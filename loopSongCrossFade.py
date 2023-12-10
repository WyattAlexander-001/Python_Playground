# pip3 install pydub
# brew install ffmpeg
# python loopSongCrossFade.py
import datetime
import os
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin" # add ffmpeg to path

import sys
print(sys.executable)
from pydub import AudioSegment

# Load the song
song_path = "audio/summer.mp3" 
song = AudioSegment.from_file(song_path)

# Crossfade duration
crossfade_duration = 5000  # 5 seconds in milliseconds

# Apply crossfade at the beginning and end
faded_in = song.fade_in(crossfade_duration)
song_with_crossfade = faded_in.fade_out(crossfade_duration)

# Calculate how many times to loop the song to fill 1 hour
one_hour = 3600000  # 1 hour in milliseconds
loop_count = one_hour // len(song)

# Create a loop for 1 hour
full_loop = song_with_crossfade
for _ in range(loop_count - 1):
    full_loop = full_loop.append(song_with_crossfade, crossfade=crossfade_duration)

# Trim the loop to exactly 1 hour
one_hour_track = full_loop[:one_hour]

# Extract the base name of the original song and create a unique file name
original_song_name = os.path.splitext(os.path.basename(song_path))[0] # Song Name without extension
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Current time in YYYY-MM-DD_HH-MM-SS format
file_name = f"{original_song_name}_1hr_version_{current_time}.mp3"  # Final file name
export_dir = "exports"
if not os.path.exists(export_dir):
    os.makedirs(export_dir)
export_path = os.path.join(export_dir, file_name)

# Export the 1-hour loop
one_hour_track.export(export_path, format="mp3")

print(f"1-hour track created and saved to: {export_path}")

