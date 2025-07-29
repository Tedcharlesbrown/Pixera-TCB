#WRITTEN BY: Ted Charles Brown

from PixeraPy import Pixera, API
from time import sleep

if __name__ == "__main__":
    ip = "127.0.0.1"  # Replace with your Pixera system's IP address
    port = 1400  # Replace with your Pixera system's port if different

    pixera = Pixera(ip, port)
    api = API()
    
    TIME_CUE_ATLANTA = 0.0
    TIME_CUE_LOSANGELES = 1200.0

    handle_timeline1 = pixera.send(api.getTimelineAtIndex(0))
    print(handle_timeline1)
    # output = pixera.send(api.Timeline.applyCueWithName(timeline1, "First Scene", 0))
    
    
    # ---------------------------- ENTER PREIVEW EDIT ---------------------------- #
    # output = pixera.send(api.Timeline.startPreviewEdit(handle_timeline1, TIME_CUE_LOSANGELES), verbose=True)
    # sleep(1)
    
    # ----------------------- SET ANOTHER PREVIEW POSITION ----------------------- #
    # output = pixera.send(api.Timeline.startPreviewEdit(handle_timeline1, TIME_CUE_ATLANTA), verbose=True)
    # sleep(1)
    
    # -------------------------- TRY TO MOVE NOWPOINTER -------------------------- #
    # output = pixera.send(api.Timeline.setCurrentTime(handle_timeline1, TIME_CUE_ATLANTA), verbose=True)
    # sleep(1)
    
    # ----------------------------- END PREVIEW EDIT ----------------------------- #
    output = pixera.send(api.Timeline.endPreviewEdit(handle_timeline1, True, 1000))
    print(f"End Preview Edit Output: {output}")
    sleep(2)
    output = pixera.send(api.Timeline.play(handle_timeline1), verbose=True)
    print(output)
    # sleep(1)
    
    # current_time = pixera.send(api.Timeline.getCurrentTime(handle_timeline1))
    # print(f"Current Time: {current_time}")
    
    # print(output)
    
    # current_time = pixera.send(api.Timeline.getCurrentTime(timeline1))
    # print(f"Current Time: {current_time}")
