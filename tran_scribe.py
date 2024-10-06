import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from faster_whisper import WhisperModel
from googletrans import Translator

def transcribe_and_translate(audio_path, target_language='en'):
    # Initialize Whisper model
    model_path = "base"
    model = WhisperModel(model_path)

    # Initialize translator
    translator = Translator()

    # Transcribe audio using Whisper model
    segments, _ = model.transcribe(audio_path, beam_size=3, task="translate")

    # Translate transcribed text to target language
    translated_segments = []
    for segment in segments:
        translated_text = translator.translate(segment.text, dest=target_language).text
        translated_segments.append(translated_text)

    return segments, translated_segments

def generate_vtt_file(segments, translated_segments, output_file):
    # Generate WebVTT content
    vtt_content = "WEBVTT\n\n"
    start_time = 0
    for segment, translated_text in zip(segments, translated_segments):
        end_time = start_time + segment.duration
        vtt_content += f"{start_time:.2f} --> {end_time:.2f}\n{translated_text}\n\n"
        start_time = end_time

    # Write content to VTT file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(vtt_content)

    print(f"WebVTT file '{output_file}' generated successfully.")

if __name__ == "__main__":
    # Path to the audio file
    audio_path = "C:\\Users\\himas\\Dhanush Trolls Tuition Teacher _ Sivakarthikeyan Best Comedy _ 3 Telugu Movie Scenes _ Shruti Haasan.mp3"

    # Target language for translation
    target_language = "hi"  # Change this to the desired target language code

    # Output file path for WebVTT
    output_file = "output.vtt"

    # Transcribe and translate
    segments, translated_segments = transcribe_and_translate(audio_path, target_language)

    # Generate WebVTT file
    generate_vtt_file(segments, translated_segments, output_file)
