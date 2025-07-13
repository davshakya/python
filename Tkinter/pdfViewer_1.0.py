import fitz  # PyMuPDF
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pyperclip
import os

class PDFTab:
    def __init__(self, notebook, filepath, app):
        self.filepath = filepath
        self.doc = fitz.open(filepath)
        self.page_num = 0
        self.zoom_factor = 1.0
        self.selected_words = []
        self.highlight_rects = []
        self.canvas_items = []
        self.words_on_page = []
        self.app = app

        self.frame = Frame(notebook)
        self.tab_name = os.path.basename(filepath)
        self.tab_id = notebook.index("end")
        self.tab_text = self.tab_name
        self.notebook = notebook

        notebook.add(self.frame, text=self.tab_label_text())

        self.canvas = Canvas(self.frame, bg="#f0f0f0")
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=TOP, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Button-3>", self.show_context_menu)

        self.context_menu = Menu(self.canvas, tearoff=0)
        self.context_menu.add_command(label="Copy", command=self.copy_selected_text)

        # Navigation and Zoom buttons
        self.button_frame = Frame(self.frame)
        self.button_frame.pack(side=BOTTOM, fill=X)
        Button(self.button_frame, text="⟵ Prev", command=self.prev_page).pack(side=LEFT, padx=2)
        Button(self.button_frame, text="Next ⟶", command=self.next_page).pack(side=LEFT, padx=2)
        Button(self.button_frame, text="Zoom In +", command=self.zoom_in).pack(side=LEFT, padx=2)
        Button(self.button_frame, text="Zoom Out -", command=self.zoom_out).pack(side=LEFT, padx=2)
        Button(self.button_frame, text="Close Tab ✖", command=self.close_tab).pack(side=LEFT, padx=2)

        self.show_page()

    def close_tab(self):
        index = self.notebook.index(self.frame)
        self.app.close_tab(index=index)

    def tab_label_text(self):
        return f"  {self.tab_name}  ✖"

    def show_page(self):
        self.canvas.delete("all")
        self.canvas_items.clear()

        page = self.doc.load_page(self.page_num)
        mat = fitz.Matrix(self.zoom_factor, self.zoom_factor)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        photo = ImageTk.PhotoImage(img)

        self.canvas.image = photo
        self.canvas.create_image(0, 0, image=photo, anchor=NW)
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        self.page = page
        self.words_on_page = page.get_text("words")
        self.clear_selection()

    def zoom_in(self):
        self.zoom_factor += 0.2
        self.show_page()

    def zoom_out(self):
        if self.zoom_factor > 0.4:
            self.zoom_factor -= 0.2
            self.show_page()

    def next_page(self):
        if self.page_num < len(self.doc) - 1:
            self.page_num += 1
            self.show_page()

    def prev_page(self):
        if self.page_num > 0:
            self.page_num -= 1
            self.show_page()

    def on_mouse_wheel(self, event):
        if event.state & 0x0004:
            self.zoom_in() if event.delta > 0 else self.zoom_out()
        else:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_click(self, event):
        self.canvas.focus_set()
        self.clear_selection()
        self.select_word(event)

    def on_drag(self, event):
        self.select_word(event)

    def select_word(self, event):
        real_x = event.x / self.zoom_factor
        real_y = event.y / self.zoom_factor
        for w in self.words_on_page:
            x0, y0, x1, y1 = w[0:4]
            word = w[4]
            rect = (x0, y0, x1, y1)
            if x0 <= real_x <= x1 and y0 <= real_y <= y1 and rect not in self.highlight_rects:
                self.selected_words.append(word)
                self.highlight_rects.append(rect)
                self.draw_highlight(rect)

    def draw_highlight(self, rect):
        x0, y0, x1, y1 = [v * self.zoom_factor for v in rect]
        item = self.canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", stipple="gray25", outline="orange", width=1)
        self.canvas_items.append(item)

    def clear_selection(self):
        self.selected_words.clear()
        self.highlight_rects.clear()
        for item in self.canvas_items:
            self.canvas.delete(item)
        self.canvas_items.clear()

    def copy_selected_text(self, event=None):
        if self.selected_words:
            text = " ".join(self.selected_words)
            try:
                self.app.root.clipboard_clear()
                self.app.root.clipboard_append(text)
                self.app.root.update()
            except:
                pyperclip.copy(text)
        else:
            messagebox.showwarning("No selection", "Select text to copy.")

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def highlight_selection(self):
        if not self.highlight_rects:
            messagebox.showwarning("No selection", "Select text to highlight.")
            return
        for rect in self.highlight_rects:
            r = fitz.Rect(rect)
            self.page.add_highlight_annot(r)
        self.doc.save("highlighted_output.pdf", incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
        messagebox.showinfo("Highlighted", "Saved to 'highlighted_output.pdf'.")

class PDFViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lalita PDF Viewer")
        ico_path = os.path.join(os.path.dirname(__file__), "1.ico")
        if os.path.exists(ico_path):
            try:
                self.root.iconbitmap(ico_path)
            except Exception as e:
                print(f"Icon load error: {e}")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=BOTH, expand=True)
        self.tabs = []
        self.notebook.bind("<<NotebookTabChanged>>", self.update_tab_styles)

        self.root.bind_all("<Control-c>", self.copy_text_event)
        self.notebook.bind("<Button-1>", self.check_tab_close)

        self.create_menu()

    def check_tab_close(self, event):
        x, y = event.x, event.y
        for i in range(len(self.tabs)):
            bbox = self.notebook.bbox(i)
            if bbox:
                x1, y1, w, h = bbox
                if x1 + w - 25 <= x <= x1 + w and y1 <= y <= y1 + h:
                    self.close_tab(index=i)
                    break

    def copy_text_event(self, event):
        self.copy_text()

    def create_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open PDF", command=self.open_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Highlight", command=self.highlight_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        nav_menu = Menu(menu_bar, tearoff=0)
        nav_menu.add_command(label="Zoom In", command=self.zoom_in)
        nav_menu.add_command(label="Zoom Out", command=self.zoom_out)
        nav_menu.add_command(label="Next Page", command=self.next_page)
        nav_menu.add_command(label="Previous Page", command=self.prev_page)
        menu_bar.add_cascade(label="View", menu=nav_menu)

        self.root.config(menu=menu_bar)

    def get_active_tab(self):
        index = self.notebook.index(self.notebook.select())
        return self.tabs[index] if index < len(self.tabs) else None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not file_path or not file_path.endswith(".pdf"):
            messagebox.showerror("Invalid file", "Please select a valid PDF file.")
            return
        tab = PDFTab(self.notebook, file_path, self)
        self.tabs.append(tab)
        self.update_tab_styles()

    def copy_text(self):
        tab = self.get_active_tab()
        if tab:
            tab.copy_selected_text()

    def highlight_text(self):
        tab = self.get_active_tab()
        if tab:
            tab.highlight_selection()

    def zoom_in(self):
        tab = self.get_active_tab()
        if tab:
            tab.zoom_in()

    def zoom_out(self):
        tab = self.get_active_tab()
        if tab:
            tab.zoom_out()

    def next_page(self):
        tab = self.get_active_tab()
        if tab:
            tab.next_page()

    def prev_page(self):
        tab = self.get_active_tab()
        if tab:
            tab.prev_page()

    def close_tab(self, index=None):
        if index is None:
            index = self.notebook.index(self.notebook.select())
        if index < len(self.tabs):
            self.notebook.forget(index)
            del self.tabs[index]
            self.update_tab_styles()

    def update_tab_styles(self, event=None):
        for i in range(len(self.tabs)):
            tab_text = self.tabs[i].tab_label_text()
            self.notebook.tab(i, text=tab_text)

if __name__ == "__main__":
    root = Tk()
    app = PDFViewerApp(root)
    root.geometry("1000x750")
    root.mainloop()
