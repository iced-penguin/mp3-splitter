import argparse
from pydub import AudioSegment
from pydub.silence import split_on_silence

class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("src", help="mp3 source file")
        parser.add_argument("dst", help="mp3 destination file")
        parser.add_argument("-t", "--threshold", help="thredhold for separation in milliseconds", default=200, dest="threshold", type=int)
        parser.add_argument("--ignore-first", help="ignore first silence", action="store_true", dest="ignore_first")
        args = parser.parse_args()

        self.src_file = args.src
        self.dst_file = args.dst
        self.threshold = args.threshold
        self.ignore_first_silence = args.ignore_first


def insert_pause(src_sound, args: Arguments):
    chunks = split_on_silence(src_sound, min_silence_len=args.threshold, silence_thresh=-32, keep_silence=True)
    num_chunks = len(chunks)

    dst_sound = AudioSegment.empty()
    for i, chunk in enumerate(chunks):
        if (i == 0 and args.ignore_first_silence) or i == num_chunks - 1:
            dst_sound += chunk
        else:
            # TODO: ポーズ長を調節する機能を追加するか検討
            dst_sound += chunk + AudioSegment.silent(len(chunk))
    
    return dst_sound


if __name__ == '__main__':
    args = Arguments()
    print("{} -> {}".format(args.src_file, args.dst_file))
    src_sound = AudioSegment.from_mp3(args.src_file)
    print("Converting...")
    dst_sound = insert_pause(src_sound, args)
    dst_sound.export(args.dst_file)
    print("Done")