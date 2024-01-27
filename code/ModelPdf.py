import pdfkit
import os


def path_wkhtmltopdf() -> str:
    '''
    wkhtmltopdfの実行ファイルのパスを返す

    リポジトリをクローンしたディレクトリに wkhtmltox\\bin\\wkhtmltopdf.exe があるものとしている
    '''
    dir = os.path.dirname(os.path.abspath(__file__))
    path_wkhtmltopdf = dir + '\\..\\wkhtmltox\\bin\\wkhtmltopdf.exe'
    # print(path_wkhtmltopdf)
    return path_wkhtmltopdf


def html_files_to_pdf(htmlfilelist: list, destfile: str, header: str = None, footer: str = None):
    """
    htmlfilelist : HTML file list
    """
    # wkhtmltopdfの実行ファイルのパスの指定
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf())

    # PDF化のオプションを設定
    options = {
        'disable-javascript': "",
        'page-size': 'A4',
        'margin-top': '0.25in',
        'margin-right': '0.10in',
        'margin-bottom': '0.25in',
        'margin-left': '0.10in',
        'zoom': '1.0',
        'encoding': "UTF-8",
        "enable-local-file-access": "",
        'header-font-size': 8,
        'header-line': '',
        'header-spacing': '2',
        # 'header-right' : '[date]',
        "footer-right": "[page]/[topage]",
        'footer-font-size': 8,
        'footer-line': '',
        'footer-spacing': '2',
    }

    if header != None:
        options['header-center'] = header

    if footer != None:
        options['footer-center'] = footer

    # HTML→PDF変換の実行
    pdfkit.from_file(htmlfilelist, destfile, configuration=config, options=options)
