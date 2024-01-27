import os, io, sys
import pathlib
import ModelPdf as pdf
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def getdirfiles(dir_path: str, wildcard: str) -> list:
    p_temp = pathlib.Path(dir_path)
    foundfiles = list(p_temp.glob(wildcard))
    return foundfiles


if __name__ == '__main__':
    dir = sys.argv[1]
    print(os.path.abspath(os.curdir), flush=True)
    outfile = os.path.abspath(os.curdir) + "\\" + os.path.basename(dir) + '.pdf'
    print('ディレクトリ内のすべてのHTMLファイルを結合してひとつのPDFにします', flush=True)
    print(f'    対象ディレクトリ: {dir}', flush=True)
    print(f'    出力先ファイル名: {outfile}', flush=True)
    print(f'    --------------------------------------------------------------------------', flush=True)

    # dir = "C:\\home\\repos\\html_pdf\\_samples\\sampleA"
    htmlfiles = getdirfiles(dir, '**/*.html')
    htmllist = []
    for htmlfile in htmlfiles:
        htmllist.append(str(htmlfile.absolute()))
        print(f'    結合対象ファイル: {str(htmlfile.absolute())}', flush=True)
    print(f'    --------------------------------------------------------------------------', flush=True)
        
    pdf.html_files_to_pdf(htmllist, outfile, "", "")
    print(f'{outfile} にPDFを作成しました', flush=True)
    print('', flush=True)
