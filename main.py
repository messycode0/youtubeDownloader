import PySimpleGUI as sg

from rich.console import Console

from os import system

from pytube import YouTube as youtube


def main():
    file_output_name = "Output"
    print("starting Console Rich")
    console = Console()
    system("cls")
    console.log("started Rich Console")

    sg.theme("DarkRed1")

    settings_layout = [
        [sg.Radio("Best", group_id="RAD1", default=True, key="-type1-"),
         sg.Radio("Worst", group_id="RAD1", default=False, key="-type2-"),
         sg.Radio("Audio", group_id="RAD1", default=False, key="-type3-")],
        [sg.Text("Where its saved: "),
         sg.Input(key="-WhereItSave-", change_submits=True, default_text="if empty, will be next to the program home"),
         sg.FolderBrowse()],
    ]

    video_info_layout = [
        [sg.Text("Name :"), sg.Text("", key="-videoNameInfo-")],
        [sg.Text("Author :"), sg.Text("", key="-videoAuthorInfo-")],
        [sg.Text("Views :"), sg.Text("", key="-videoViewsInfo-")],
        [sg.Text("Description :"),
         sg.Frame("Description", layout=[[sg.Button("click to see Description", key="-lookAtDec-")]])],
        [sg.Text("Duration :"), sg.Text("", key="-videoDurationInfo-")],

    ]

    settings_col = sg.Column([
        [sg.Frame("Options", settings_layout)],
        [sg.Frame("Video Information", video_info_layout)]
    ])

    normale_col = sg.Column([
        [sg.Text("Enter the Name of the file")],
        [sg.InputText(key="-fileName-")],
        [sg.Text("Enter the URL of the Video you want to download")],
        [sg.InputText(key="-url-", enable_events=True)],
        [sg.Button("Enter", key="-enter-btn-")]
    ])

    layout = [
        [normale_col, settings_col]
    ]

    window = sg.Window("youTube Downloader", layout=layout)
    console.log("made the window")
    console.log("starting the While loop")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            console.log("User pressed Exit")
            console.print("Exiting...", style="b u i blink red on white")
            break
        if event == "-enter-btn-":
            console.log("setting the -fileName- into file_output_name")
            file_output_name = values["-fileName-"]
            print(values["-url-"])
            print(values["-type1-"])
            print(values["-type2-"])
            print(values["-type3-"])
            console.log("checking the Path")
            if values["-WhereItSave-"] == "if empty, will be next to the program home":
                values["-WhereItSave-"] = "./"
            try:
                video_obj = youtube(values["-url-"])
                console.log("video Name: ", video_obj.title)
                if values["-type1-"]:
                    temp = file_output_name
                    file_output_name = file_output_name + ".mp4"
                    video_obj.streams.get_highest_resolution().download(filename=file_output_name,
                                                                        output_path=values["-WhereItSave-"])
                    file_output_name = temp
                    sg.popup("your video has successfully downloaded\n\ndownload name: " + file_output_name + "\nlocation: " + values["-WhereItSave-"])

                elif values["-type2-"]:
                    temp = file_output_name
                    file_output_name = file_output_name + ".mp4"
                    video_obj.streams.get_lowest_resolution().download(filename=file_output_name,
                                                                       output_path=values["-WhereItSave-"])
                    file_output_name = temp
                    sg.popup("your video has successfully downloaded\n\ndownload name: " + file_output_name + "\nlocation: " + values["-WhereItSave-"])

                elif values["-type3-"]:
                    temp = file_output_name
                    file_output_name = file_output_name + ".mp3"
                    video_obj.streams.get_audio_only().download(filename=file_output_name,
                                                                output_path=values["-WhereItSave-"])
                    file_output_name = temp
                    sg.popup("your audio has successfully downloaded\n\ndownload name: " + file_output_name + "\nlocation: " + values["-WhereItSave-"])

                console.log("downloaded the YouTube video called ", file_output_name)
                console.log(log_locals=True)
            except Exception as e:
                console.print("Error: ", e, style="b u i blink red on white")
                console.log(log_locals=True)
                sg.popup("Error: ", "An error has Stopped the Download...\nretry or change to a lower "
                                    "resolution\n\nEXCEPTION:\n", e)

        if event == "-url-":
            try:
                video_obj = youtube(values["-url-"])
                console.log("video Name: ", video_obj.title)
                console.log("video Author: ", video_obj.author)
                console.log("video Views: ", video_obj.views)
                console.log("video Description: ", video_obj.description)

                window["-videoNameInfo-"].update(video_obj.title)
                window["-videoAuthorInfo-"].update(video_obj.author)
                window["-videoViewsInfo-"].update(video_obj.views)
                window["-videoDurationInfo-"].update(str(video_obj.length // 60) + ":" + str(video_obj.length % 60))

                # window["-videoDescriptionInfo-"].update(video_obj.description)

            except Exception as e:
                console.print("Error: ", e, style="b u i blink red on white")
            pass
        if event == "-lookAtDec-":
            try:
                video_obj = youtube(values["-url-"])
                sg.popup(video_obj.description, any_key_closes=True, grab_anywhere=True)
            except:
                pass

    pass


if __name__ == "__main__":
    print("starting...")
    main()
