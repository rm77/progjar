from chatcli import *


import flet as ft


TARGET_IP = os.getenv("SERVER_IP") or "127.0.0.1"
TARGET_PORT = os.getenv("SERVER_PORT") or "8889"
ON_WEB = os.getenv("ONWEB") or "0"


def main(page):
    def btn_click(e):
        if not cmd.value:
            cmd.error_text = "masukkan command"
            page.update()
        else:
            txt = cmd.value
            lv.controls.append(ft.Text(f"command: {txt}"))
            txt = cc.proses(txt)
            lv.controls.append(ft.Text(f"result {cc.tokenid}: {txt}"))
            cmd.value=""
            page.update()

    cc = ChatClient()


    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    cmd = ft.TextField(label="Your command")

    page.add(lv)
    page.add(cmd, ft.ElevatedButton("Send", on_click=btn_click))


if __name__=='__main__':
    if (ON_WEB=="1"):
        ft.app(target=main,view=ft.WEB_BROWSER,port=8550)
    else:
        ft.app(target=main)

