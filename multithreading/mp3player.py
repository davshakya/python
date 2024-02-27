import pygame
import os
import platform

def play_mp3(file_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    try:
        # Load the MP3 file
        pygame.mixer.music.load(file_path)

        # Play the MP3 file
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"Error playing MP3: {e}")

    # Quit Pygame mixer
    pygame.mixer.quit()

if __name__ == "__main__":
    # Replace 'your_file.mp3' with the path to your MP3 file
    mp3_file_path = "test.mp3"

    # Check the platform (Linux or Windows)
    current_platform = platform.system()

    # Windows uses different backslashes in file paths, so we convert them to forward slashes
    if current_platform == 'Windows':
        mp3_file_path = mp3_file_path.replace('\\', '/')

    # Play the MP3 file
    play_mp3(mp3_file_path)
