import streamlit as st

def main():
    st.title("Production Setup Checklist")
    
    topics = {
        "833 with Boom or Wireless Lav": [
            "Connect batteries in back of 833",
            "Connect boom to 833 with cable or wireless, connect lav receiver to 833 with cable",
            "Insert SD card in right wall",
            "Turn on matching channels trim button (button surrounded by light), turn it so input level is around -20 and peaks at -12",
            "Leave fader at 0, it only affects the mixed tracks, we’ll use automixer when needed.",
            "Turn PFL Switch to channel number (little switch between 1 and 2 etc) to see channel screen",
            "Choose Mic + Phantom + L or C or R (Usually Boom to L) if boom connected with cable, choose line, no phantom, L or C or R if Rx (receiver) is connected (Usually Lavs to R)",
            "menu->quick setup->load factory setting",
            "menu->record/play->track to media routing->turn on bottom right to BWF",
            "menu->record/play->pre roll->5 or 10 sec",
            "menu->record/play->track to media routing->make sure all is lighted on all cards (ensures POLYphonic, which will create a WAV file that includes separate track for each ISO and one for each mixed track (L and R). Can adjust differently to each card.",
            "menu->system->time/date->24 hrs",
            "menu->files->files->format SSD",
            "menu->files->files->format->SD",
            "menu->record/play->sample rate 48000",
            "menu->record/play->bit depth->24bit",
            "Menu -> Timecode/Sync -> 24 Hour Run (ToD)",
            "Menu -> Timecode/Sync -> Frame Rate->23.98 (match camera)",
            "Menu -> Timecode/Sync- > UBits (optional, if using the Denecke slate)",
            "Menu -> Automixer ->Dugan - Enabled -> Channel Selection 1–8 (blue)"
        ],
        "When You Arrive On-Set": [
            "Create a Custom folder and a Date folder to keep files organized (menu->files->take list)",
            "Label the ISO tracks using your participants’ names"
        ],
        "Connect Receiver/Transmitter": [
            "Tx - off",
            "Rx - menu->smart tune->A1-> searching",
            "Tx - on",
            "Press button to the right of the arrow on Rx and put both Infra Red eyes close until Rx says OK",
            "Connect Lav to Tx",
            "Tx gain-26 and check side lights when you talk. Should be green unless you talk very loud and then it's red",
            "Rx - set audio level to 5",
            "Tx-menu->RF On?-> YES",
            "Connect Rx to 833"
        ],
        "Sync with JB1": [
            "833 -> Menu>system>date/time>24hrs",
            "Menu>timecode sync>timecode mode>24 hrs run",
            "Menu>timecode sync>frame rate-> 23.98 (same as camera)",
            "Menu>timecode sync>set generation ubits>today's date",
            "Connect the single Limo cable side to the right wall of 833.",
            "Turn JB1 on, should say AJO.",
            "Connect OUT to the JB1.",
            "Disconnect after it is synched."
        ],
        "Camera Setup": [
            "Timecode should be set to IN.",
            "Connect JB1 to camera with BNC to BNC cable",
            "Initialize the camera: Menu > System Settings > Initialize > Load Factory Data > Yes",
            "Set Frame Rate / Frequency: Menu > System Settings > System Mode > Frequency > 23.98p or 24p",
            "Configure Sensor Mode: Menu > System Settings > System Mode > Sensor Mode > S35 5.7K",
            "Set Resolution / Main Pixel: Menu > System Settings > System Mode > Main Pixel > 4096 x 2160 or 3840 x 2160",
            "Choose Codec: Menu > System Settings > System Mode > Main Codec > 422 All-I 400M or 150M",
            "Adjust Color Settings / Gamma: Menu > System Settings > Color Settings > Main > V-Log",
            "Adjust Color Settings / Gamma: Menu > System Settings > Color Settings > lcd out > V-709",
            "Configure Shutter Speed / Shutter Angle: Menu > Camera Settings > Shutter > Mode > sec, Value > Half Shutter (1/48.0)",
            "Set ISO / Gain: Menu > Camera Settings > EI > Mode > ISO, Native ISO > 800 (daylight) ISO or 2500 (low light) ISO",
            "Adjust White Balance: Menu > Camera Settings > white->Value > (3200 indoor, 5600 outdoor, 4300 mixed. select color temperature)",
            "Format Media: Menu > Rec Settings > Cards/Media > Format Media > Slot 1, Slot 2",
            "Configure Timecode: Menu > Rec Settings > TC > Free Run or Rec Run",
            "Set Audio Inputs and Channels: Menu > Audio Settings > Audio Ch Settings > channel1 in select->input1 (probably the camera’s boom mic)",
            "Set Audio Inputs and Channels: Menu > Audio Settings > Audio input > input1 line/mic sel->mic (for camera’s boom)",
            "Set Audio Inputs and Channels: Menu > Audio Settings > Audio input > input1 mic powerl->on (for camera’s boom)",
            "Enable Pre-record Mode: Menu > Rec Settings > Pre Rec > On",
            "Reset Timecode: Menu > Rec Settings > TC > Set TC > (set all values back to zero)"
        ]
    }
    
    for topic, checklist in topics.items():
        with st.expander(topic):
            for item in checklist:
                st.checkbox(item)

if __name__ == "__main__":
    main()
