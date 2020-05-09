import os.path
import os
import re
import xlwt
# rootdir = raw_input('root dir:\n')
from pydub import AudioSegment


def main():
    rootdir = os.path.abspath(r"D:\files")
    path2 = r"D:\watermarks\fttm0.wav"
    print('absolute root path:\n*** ' + rootdir + ' ***')
    print('absolute watermark path:\n*** ' + path2 + ' ***')

    #file_list = check_file(r"D:\files")
    #book = xlwt.Workbook()
    #sheet = book.add_sheet('filename')
    #output_type = ""
    audio_length = 0
    # get watermark file
    sound2 = AudioSegment.from_file(path2)
    # conversion job
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            filenamedir = os.path.join(parent, filename)
            portion = os.path.splitext(filename)
            # check extention is .wav
            if portion[1] == ".wav":
                # make new file name and extention
                newname = portion[0] + ".mp3"
                newnamedir = os.path.split(os.path.realpath(filenamedir))[0] + "\\" + newname
                # check audio length
                sound1 = AudioSegment.from_file(filenamedir)
                time_org=len(sound1)
                time = int(time_org / 1000.0)
                # repeat_cnt = int((time - 5) / 10)
                # mix sound2 with sound1, starting at position into sound1 with loop)
                if time >= 12:
                    output = sound1.overlay(sound2, position=5000, loop=True)
                    # export audio file
                #    output.export(newnamedir, format="mp3", bitrate="320k")
                #    print("output is larger than 12 sec, with new name:      ", newnamedir)
                    output_type = "L"
                elif 3 <= time < 12:
                    output = sound1.overlay(sound2, position=3000, loop=True)
                #    output.export(newnamedir, format="mp3", bitrate="320k")
                #    print("output is between 3 sec to 12 sec, with new name: ", newnamedir)
                    output_type = "M"
                elif 0 <= time < 3:
                    output = sound1.overlay(sound2, position=200, loop=True)
                    # export audio file
                    output_type = "S"
                output.export(newnamedir, format="mp3", bitrate="320k")
                print("output_type ;    ",output_type, "    ;    length    ;    ",time_org, "    ;    filename;    ", newnamedir)
                #sheet.write(filename,0, output_string)
                #book.save("output.xls")
#
# def check_file(file_path):
#     os.chdir(file_path)
#     print(os.path.abspath(os.curdir))
#     all_file = os.listdir()
#     files = []
#     for f in all_file:
#         if os.path.isdir(f):
#             files.extend(check_file(file_path+'\\'+f))
#             os.chdir(file_path)
#         else:
#             files.append(f)
#     return files
#
# file_list = check_file(r"D:\files")

# #book = xlwt.Workbook()
# #sheet = book.add_sheet('文件名')
# i = 0
# for data in file_list:
# #    sheet.write(i,0,data)
#     i += 1
#
# #book.save('文件名搜索.xls')
#
# s = ' '.join(file_list)
# res_1 = re.findall(r'\D\d{8}\D',s)
# print(res_1)

if __name__ == '__main__':
    main()
