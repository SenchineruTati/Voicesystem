from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent

# 音声ファイルを読み込みます
audio = AudioSegment.from_file("C:\k021c1523\Python\kane.wav", format="wav")

# 無音の検出
# min_silence_len: 無音とみなす最小の長さ（ミリ秒）
# silence_thresh: 無音とみなす閾値（デシベル）
nonsilent_ranges = detect_nonsilent(audio, min_silence_len=1000, silence_thresh=-40)

# 音がある部分と無音部分のリストを作成
sound_parts = [audio[start:end] for start, end in nonsilent_ranges]

# 無音部分を取得するために音がある部分の間の無音部分を推測
silent_parts = []
previous_end = 0
for start, end in nonsilent_ranges:
    if previous_end < start:
        silent_parts.append(audio[previous_end:start])
    previous_end = end

# 最後の無音部分を追加
if previous_end < len(audio):
    silent_parts.append(audio[previous_end:len(audio)])

# 音がある部分と無音部分をそれぞれ結合
sound_audio = AudioSegment.empty()
for part in sound_parts:
    sound_audio += part

silent_audio = AudioSegment.empty()
for part in silent_parts:
    silent_audio += part

# 別のファイルに出力する
sound_audio.export("C:\k021c1523\music\output_sound_audio_file.wav", format="wav")
silent_audio.export("C:\k021c1523\music\output_silent_audio_file.wav", format="wav")

print("音がある部分と無音部分をそれぞれ別のファイルに出力しました。")
