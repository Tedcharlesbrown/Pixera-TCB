class Methods:
    GET_API_REVISION = "Pixera.Utility.getApiRevision"
    GET_HAS_FUNCTION = "Pixera.Utility.getHasFunction"
    OUTPUT_DEBUG = "Pixera.Utility.outputDebug"
    GET_LICENSE_JSON = "Pixera.Utility.getLicenseJson"
    GET_CURRENT_TIME = "Pixera.Utility.getCurrentTime"
    GET_CURRENT_TIME_AS_STRING = "Pixera.Utility.getCurrentTimeAsString"
    NOOP = "Pixera.Utility.noop"
    REQUEST_CALLBACK = "Pixera.Utility.requestCallback"
    READ_FILE_STRING = "Pixera.Utility.readFileString"
    WRITE_FILE_STRING = "Pixera.Utility.writeFileString"
    GET_ACCESS_RECIPE = "Pixera.Utility.getAccessRecipe"
    POLL_MONITORING = "Pixera.Utility.pollMonitoring"
    UNSUBSCRIBE_MONITORING_SUBJECT = "Pixera.Utility.unsubscribeMonitoringSubject"
    SUBSCRIBE_MONITORING_SUBJECT = "Pixera.Utility.subscribeMonitoringSubject"
    SET_MONITORING_EVENT_MODE = "Pixera.Utility.setMonitoringEventMode"
    MONITORING_EVENT = "Pixera.Utility.monitoringEvent"
    SET_SHOW_CONTEXT_IN_REPLIES = "Pixera.Utility.setShowContextInReplies"
    SET_MONITORING_HAS_DELIMITER = "Pixera.Utility.setMonitoringHasDelimiter"
    RUN_JS_SCRIPT = "Pixera.Utility.runJsScript"
    DYNAMIC_REBUILD_FROM_JSON_DESCRIPTION = "Pixera.Utility.dynamicRebuildFromJsonDescription"
    GET_CONVEYOR = "Pixera.Network.getConveyor"
    SET_TRANSPORT_MODE_ON_TIMELINE_AT_INDEX = "Pixera.Compound.setTransportModeOnTimelineAtIndex"
    SET_TRANSPORT_MODE_ON_TIMELINE = "Pixera.Compound.setTransportModeOnTimeline"
    TOGGLE_TRANSPORT = "Pixera.Compound.toggleTransport"
    GET_TRANSPORT_MODE_ON_TIMELINE = "Pixera.Compound.getTransportModeOnTimeline"
    SET_OPACITY_ON_TIMELINE = "Pixera.Compound.setOpacityOnTimeline"
    GET_OPACITY_ON_TIMELINE = "Pixera.Compound.getOpacityOnTimeline"
    START_FIRST_TIMELINE = "Pixera.Compound.startFirstTimeline"
    PAUSE_FIRST_TIMELINE = "Pixera.Compound.pauseFirstTimeline"
    STOP_FIRST_TIMELINE = "Pixera.Compound.stopFirstTimeline"
    SET_POS_VALUE = "Pixera.Compound.setPosValue"
    SET_POS_VALUE_X_Y = "Pixera.Compound.setPosValueXY"
    SET_PARAM_VALUE = "Pixera.Compound.setParamValue"
    APPLY_CUE_AT_INDEX_ON_TIMELINE_AT_INDEX = "Pixera.Compound.applyCueAtIndexOnTimelineAtIndex"
    APPLY_CUE_NUMBER_ON_TIMELINE_AT_INDEX = "Pixera.Compound.applyCueNumberOnTimelineAtIndex"
    APPLY_CUE_NUMBER_ON_TIMELINE = "Pixera.Compound.applyCueNumberOnTimeline"
    APPLY_CUE_ON_TIMELINE = "Pixera.Compound.applyCueOnTimeline"
    ADD_RESOURCE_TO_FOLDER = "Pixera.Compound.addResourceToFolder"
    ASSIGN_RESOURCE_TO_LAYER = "Pixera.Compound.assignResourceToLayer"
    REFRESH_RESOURCE = "Pixera.Compound.refreshResource"
    SET_TRANSPORT_MODE_ON_LAYER = "Pixera.Compound.setTransportModeOnLayer"
    GET_TRANSPORT_MODE_ON_LAYER = "Pixera.Compound.getTransportModeOnLayer"
    GET_RESOURCE_ASSIGNED_TO_LAYER = "Pixera.Compound.getResourceAssignedToLayer"
    ASSIGN_RESOURCE_TO_CLIP_AT_TIME_BY_DMX_ID = "Pixera.Compound.assignResourceToClipAtTimeByDmxId"
    ASSIGN_RESOURCE_TO_CLIP_AT_H_M_S_F_STRING_BY_DMX_ID = "Pixera.Compound.assignResourceToClipAtHMSFStringByDmxId"
    ASSIGN_RESOURCE_TO_CLIP_AT_H_M_S_F_BY_DMX_ID = "Pixera.Compound.assignResourceToClipAtHMSFByDmxId"
    SET_CURRENT_TIME_OF_TIMELINE = "Pixera.Compound.setCurrentTimeOfTimeline"
    SET_CURRENT_TIME_OF_TIMELINE_IN_SECONDS = "Pixera.Compound.setCurrentTimeOfTimelineInSeconds"
    SET_CURRENT_TIME_AND_TRANSPORT_MODE_OF_TIMELINE_IN_SECONDS = "Pixera.Compound.setCurrentTimeAndTransportModeOfTimelineInSeconds"
    GET_FPS_OF_TIMELINE = "Pixera.Compound.getFpsOfTimeline"
    GET_CURRENT_TIME_OF_TIMELINE = "Pixera.Compound.getCurrentTimeOfTimeline"
    GET_CURRENT_TIME_OF_TIMELINE_IN_SECONDS = "Pixera.Compound.getCurrentTimeOfTimelineInSeconds"
    GET_CURRENT_H_M_S_F_OF_TIMELINE = "Pixera.Compound.getCurrentHMSFOfTimeline"
    GET_CURRENT_COUNTDOWN_OF_TIMELINE = "Pixera.Compound.getCurrentCountdownOfTimeline"
    GET_CURRENT_COUNTDOWN_H_M_S_F_OF_TIMELINE = "Pixera.Compound.getCurrentCountdownHMSFOfTimeline"
    START_OPACITY_ANIMATION_OF_TIMELINE = "Pixera.Compound.startOpacityAnimationOfTimeline"
    CREATE_CLIP_ON_LAYER_AT_TIME_WITH_RESOURCE = "Pixera.Compound.createClipOnLayerAtTimeWithResource"
    REMOVE_CLIP_ON_LAYER_WITH_INDEX = "Pixera.Compound.removeClipOnLayerWithIndex"
    REMOVE_ALL_CLIPS_ON_LAYER = "Pixera.Compound.removeAllClipsOnLayer"
    GET_CLIP_DURATION_IN_SECONDS_WITH_INDEX = "Pixera.Compound.getClipDurationInSecondsWithIndex"
    GET_CLIP_DURATION_IN_FRAMES_WITH_INDEX = "Pixera.Compound.getClipDurationInFramesWithIndex"
    GET_CLIP_TIME_IN_SECONDS_WITH_INDEX = "Pixera.Compound.getClipTimeInSecondsWithIndex"
    GET_CLIP_END_TIME_IN_SECONDS_WITH_INDEX = "Pixera.Compound.getClipEndTimeInSecondsWithIndex"
    GET_RESOURCE_DURATION_IN_SECONDS = "Pixera.Compound.getResourceDurationInSeconds"
    GET_PARAM_VALUE = "Pixera.Compound.getParamValue"
    SET_TIMECODE_INPUT = "Pixera.Compound.setTimecodeInput"
    TAKE_OVER_ALL_CLIENTS = "Pixera.Compound.takeOverAllClients"
    SET_PAUSE_SMPTE_INPUT = "Pixera.Compound.setPauseSmpteInput"
    CLOSE_APP = "Pixera.Session.closeApp"
    LOAD_PROJECT = "Pixera.Session.loadProject"
    SAVE_PROJECT = "Pixera.Session.saveProject"
    SAVE_PROJECT_AS = "Pixera.Session.saveProjectAs"
    GET_PROJECT_NAME = "Pixera.Session.getProjectName"
    SET_PROJECT_NAME = "Pixera.Session.setProjectName"
    GET_PROJECT_DIRECTORY = "Pixera.Session.getProjectDirectory"
    GET_CONTROL_MULTI_USER_SESSION_NAME = "Pixera.Session.getControlMultiUserSessionName"
    SHUTDOWN_SYSTEM = "Pixera.Session.shutdownSystem"
    GET_LIVE_SYSTEM_IPS = "Pixera.Session.getLiveSystemIps"
    GET_LIVE_SYSTEM_STATE = "Pixera.Session.getLiveSystemState"
    LIVE_SYSTEM_STATE_CHANGE = "Pixera.Session.liveSystemStateChange"
    SHUTDOWN_LIVE_SYSTEM = "Pixera.Session.shutdownLiveSystem"
    WAKE_LIVE_SYSTEM = "Pixera.Session.wakeLiveSystem"
    GET_LIVE_SYSTEM_MAC_ADDRESS = "Pixera.Session.getLiveSystemMacAddress"
    START_LIVE_SYSTEM = "Pixera.Session.startLiveSystem"
    START_LIVE_SYSTEMS = "Pixera.Session.startLiveSystems"
    STOP_LIVE_SYSTEM = "Pixera.Session.stopLiveSystem"
    STOP_LIVE_SYSTEMS = "Pixera.Session.stopLiveSystems"
    RESTART_LIVE_SYSTEM = "Pixera.Session.restartLiveSystem"
    RESTART_LIVE_SYSTEMS = "Pixera.Session.restartLiveSystems"
    REMOTE_SYSTEM_STATE_CHANGE = "Pixera.Session.remoteSystemStateChange"
    GET_REMOTE_SYSTEM_IPS = "Pixera.Session.getRemoteSystemIps"
    GET_REMOTE_SYSTEM_STATE = "Pixera.Session.getRemoteSystemState"
    SET_VIDEO_STREAM_ACTIVE_STATE = "Pixera.Session.setVideoStreamActiveState"
    GET_VIDEO_STREAM_ACTIVE_STATE = "Pixera.Session.getVideoStreamActiveState"
    GET_DEFAULT_CLIP_DURATIONS_AS_JSON_STRING = "Pixera.Session.getDefaultClipDurationsAsJsonString"
    GET_LIVE_SYSTEMS = "Pixera.LiveSystems.getLiveSystems"
    LIVE_SYSTEM_NOT_AVAILABLE = "Pixera.LiveSystems.liveSystemNotAvailable"
    GET_MULTI_USER_MEMBERS = "Pixera.LiveSystems.getMultiUserMembers"
    GET_SCREEN_WITH_NAME = "Pixera.Screens.getScreenWithName"
    SET_NAMED_SCREEN_POSITION = "Pixera.Screens.setNamedScreenPosition"
    GET_SCREENS = "Pixera.Screens.getScreens"
    GET_SCREEN_NAMES = "Pixera.Screens.getScreenNames"
    GET_FIRST_TIMELINE_WITH_HOME_SCREEN = "Pixera.Screens.getFirstTimelineWithHomeScreen"
    GET_STUDIO_CAMERAS = "Pixera.Screens.getStudioCameras"
    GET_PROJECTOR_WITH_NAME = "Pixera.Projectors.getProjectorWithName"
    GET_PROJECTORS = "Pixera.Projectors.getProjectors"
    GET_PROJECTOR_NAMES = "Pixera.Projectors.getProjectorNames"
    GET_RESOURCES = "Pixera.Resources.getResources"
    GET_RESOURCE_FOLDER_WITH_NAME_PATH = "Pixera.Resources.getResourceFolderWithNamePath"
    GET_RESOURCE_FOLDERS = "Pixera.Resources.getResourceFolders"
    GET_TRANSCODING_FOLDERS = "Pixera.Resources.getTranscodingFolders"
    GET_JSON_DESCRIP = "Pixera.Resources.getJsonDescrip"
    GET_TIMELINE_AT_INDEX = "Pixera.Timelines.getTimelineAtIndex"
    GET_TIMELINE_FROM_NAME = "Pixera.Timelines.getTimelineFromName"
    GET_TIMELINES = "Pixera.Timelines.getTimelines"
    GET_TIMELINE_NAMES = "Pixera.Timelines.getTimelineNames"
    GET_TIMELINES_SELECTED = "Pixera.Timelines.getTimelinesSelected"
    CREATE_TIMELINE = "Pixera.Timelines.createTimeline"
    GET_NODE_FROM_ID = "Pixera.Timelines.getNodeFromId"
    SET_MARKER_POSITIONS = "Pixera.Calibration.setMarkerPositions"
    LOAD_DEVICE_UI = "Pixera.WebViews.loadDeviceUi"
    ACTIVATE_PREVIOUS_FUNC = "Pixera.WebViews.activatePreviousFunc"
    ACTIVATE_NEXT_FUNC = "Pixera.WebViews.activateNextFunc"
    GET_LAST_ACTIVATED_FUNC = "Pixera.WebViews.getLastActivatedFunc"
    DEVICE_ACTIVATED = "Pixera.WebViews.deviceActivated"
    FUNC_ACTIVATED = "Pixera.WebViews.funcActivated"
    SET_FUNC_BODY_STATE = "Pixera.WebViews.setFuncBodyState"
    GET_FUNC_BODY_STATE = "Pixera.WebViews.getFuncBodyState"
    SET_TAG = "Pixera.WebViews.setTag"
    SET_EDITOR_IS_USING_BLOCKS = "Pixera.WebViews.setEditorIsUsingBlocks"
    GET_COMBO_BOX_WITH_ID = "Pixera.Ui.getComboBoxWithId"
    SET_APP_MODE = "Pixera.Ui.setAppMode"
    GET_APP_MODE = "Pixera.Ui.getAppMode"
    GET_DISPLAY_TESTPATTERN = "Pixera.Ui.getDisplayTestpattern"
    SET_DISPLAY_TESTPATTERN = "Pixera.Ui.setDisplayTestpattern"
    GET_PREVIEW_CAMERA_AS_JSON_STRING = "Pixera.Ui.getPreviewCameraAsJsonString"
    SET_PREVIEW_CAMERA_AS_JSON_STRING = "Pixera.Ui.setPreviewCameraAsJsonString"
    SET_DISABLE_CONTENT_RENDERING = "Pixera.Ui.setDisableContentRendering"
    GET_IS_CONTENT_RENDERING_DISABLED = "Pixera.Ui.getIsContentRenderingDisabled"
    SET_DISABLE_WORKSPACE_RENDERING = "Pixera.Ui.setDisableWorkspaceRendering"
    GET_IS_WORKSPACE_RENDERING_DISABLED = "Pixera.Ui.getIsWorkspaceRenderingDisabled"
    SET_REGISTERED = "Pixera.Direct.setRegistered"
    RELOAD_REGISTERED = "Pixera.Direct.reloadRegistered"
    REGISTER_SCREEN = "Pixera.Direct.registerScreen"
    REGISTER_PARAM = "Pixera.Direct.registerParam"
    REGISTER_CAMERA = "Pixera.Direct.registerCamera"
    REGISTER_PERSPECTIVE = "Pixera.Direct.registerPerspective"