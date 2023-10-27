
# Protocol Overview
This documentation describes revision 349 of the API.

The Pixera API uses the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol.

Pixera API test application by Benni Müller can be found [here](http://www.benni-m.de/index.html#projects).

## Protocols

 - JSON/TCP
   - Requires header with prefix and message size
     - 'pxr1' + 4-byte size (least significant byte first)
       - `pxr1R000{{"jsonrpc": "2.0","id": 1,"method": "Pixera.Utility.getApiRevision"}}`
 - JSON/TDP(dl)
   - Requires delimiter
     - 0xPX
       - `{"jsonrpc": "2.0","id": 1,"method": "Pixera.Utility.getApiRevision"}0xPX`

# API Overview
## Pixera

### Utility

**GET API REVISION**

`Pixera.Utility.getApiRevision`

- **Return Values**:
  - `int` : *int*

---

**GET HAS FUNCTION**

`Pixera.Utility.getHasFunction`

- **Parameters**:
  - `functionName` : *string*

- **Return Values**:
  - `bool` : *bool*

---

**OUTPUT DEBUG**

`Pixera.Utility.outputDebug`

- **Parameters**:
  - `message` : *string*

- **Return Values**:
  - `string` : *string*

---

**GET LICENSE JSON**

`Pixera.Utility.getLicenseJson`

- **Return Values**:
  - `string` : *string*

---

**GET CURRENT TIME**

`Pixera.Utility.getCurrentTime`

- **Return Values**:
  - `double` : *double*

---

**GET CURRENT TIME AS STRING**

`Pixera.Utility.getCurrentTimeAsString`

- **Return Values**:
  - `string` : *string*

---

**NOOP**

`Pixera.Utility.noop`

- **Return Values**:
  - `null` : *null*

---

**REQUEST CALLBACK**

`Pixera.Utility.requestCallback`

- **Parameters**:
  - `functionName` : *string*

- **Return Values**:
  - `null` : *null*

---

**READ FILE STRING**

`Pixera.Utility.readFileString`

- **Parameters**:
  - `path` : *string*

- **Return Values**:
  - `string` : *string*

---

**WRITE FILE STRING**

`Pixera.Utility.writeFileString`

- **Parameters**:
  - `path` : *string*
  - `fileStr` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET ACCESS RECIPE**

`Pixera.Utility.getAccessRecipe`

- **Parameters**:
  - `hdlPath` : *string*

- **Return Values**:
  - `string` : *string*

---

**POLL MONITORING**

`Pixera.Utility.pollMonitoring`

- **Return Values**:
  - `string` : *string*

---

**UNSUBSCRIBE MONITORING SUBJECT**

`Pixera.Utility.unsubscribeMonitoringSubject`

- **Parameters**:
  - `subject` : *string*

- **Return Values**:
  - `bool` : *bool*

---

**SUBSCRIBE MONITORING SUBJECT**

`Pixera.Utility.subscribeMonitoringSubject`

- **Parameters**:
  - `subject` : *string*

- **Return Values**:
  - `bool` : *bool*

---

**SET MONITORING EVENT MODE**

`Pixera.Utility.setMonitoringEventMode`

- **Parameters**:
  - `mode` : *string*

- **Return Values**:
  - `bool` : *bool*

---

**MONITORING EVENT**

`Pixera.Utility.monitoringEvent`

- **Parameters**:
  - `eventDescription` : *string*

- **Return Values**:
  - `null` : *null*

---

**SET SHOW CONTEXT IN REPLIES**

`Pixera.Utility.setShowContextInReplies`

- **Parameters**:
  - `doShow` : *bool*

- **Return Values**:
  - `bool` : *bool*

---

**SET MONITORING HAS DELIMITER**

`Pixera.Utility.setMonitoringHasDelimiter`

- **Parameters**:
  - `hasDelimiter` : *bool*

- **Return Values**:
  - `bool` : *bool*

---

**RUN JS SCRIPT**

`Pixera.Utility.runJsScript`

- **Parameters**:
  - `jsFunction` : *string*
  - `jsCode` : *string*

- **Return Values**:
  - `string` : *string*

---

**DYNAMIC REBUILD FROM JSON DESCRIPTION**

`Pixera.Utility.dynamicRebuildFromJsonDescription`

- **Parameters**:
  - `deviceName` : *string*
  - `jsonDescription` : *string*
  - `folder` : *string*

- **Return Values**:
  - `null` : *null*

---

### Network

**GET CONVEYOR**

`Pixera.Network.getConveyor`

- **Parameters**:
  - `conveyorName` : *string*

- **Return Values**:
  - `handle` : *handle*

---

### Compound

**SET TRANSPORT MODE ON TIMELINE AT INDEX**

`Pixera.Compound.setTransportModeOnTimelineAtIndex`

- **Parameters**:
  - `index` : *int*
  - `mode` : *int*

- **Return Values**:
  - `bool` : *bool*

---

**SET TRANSPORT MODE ON TIMELINE**

`Pixera.Compound.setTransportModeOnTimeline`

- **Parameters**:
  - `timelineName` : *string*
  - `mode` : *int*

- **Return Values**:
  - `null` : *null*

---

**TOGGLE TRANSPORT**

`Pixera.Compound.toggleTransport`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET TRANSPORT MODE ON TIMELINE**

`Pixera.Compound.getTransportModeOnTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `int` : *int*

---

**SET OPACITY ON TIMELINE**

`Pixera.Compound.setOpacityOnTimeline`

- **Parameters**:
  - `timelineName` : *string*
  - `opacity` : *double*

- **Return Values**:
  - `null` : *null*

---

**GET OPACITY ON TIMELINE**

`Pixera.Compound.getOpacityOnTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `double` : *double*

---

**START FIRST TIMELINE**

`Pixera.Compound.startFirstTimeline`

- **Return Values**:
  - `null` : *null*

---

**PAUSE FIRST TIMELINE**

`Pixera.Compound.pauseFirstTimeline`

- **Return Values**:
  - `null` : *null*

---

**STOP FIRST TIMELINE**

`Pixera.Compound.stopFirstTimeline`

- **Return Values**:
  - `null` : *null*

---

**SET POS VALUE**

`Pixera.Compound.setPosValue`

- **Parameters**:
  - `val` : *double*

- **Return Values**:
  - `null` : *null*

---

**SET POS VALUE XY**

`Pixera.Compound.setPosValueXY`

- **Parameters**:
  - `valX` : *double*
  - `valY` : *double*

- **Return Values**:
  - `null` : *null*

---

**SET PARAM VALUE**

`Pixera.Compound.setParamValue`

- **Parameters**:
  - `path` : *string*
  - `value` : *double*

- **Return Values**:
  - `null` : *null*

---

**APPLY CUE AT INDEX ON TIMELINE AT INDEX**

`Pixera.Compound.applyCueAtIndexOnTimelineAtIndex`

- **Parameters**:
  - `cueIndex` : *int*
  - `timelineIndex` : *int*

- **Return Values**:
  - `null` : *null*

---

**APPLY CUE NUMBER ON TIMELINE AT INDEX**

`Pixera.Compound.applyCueNumberOnTimelineAtIndex`

- **Parameters**:
  - `cueNumber` : *int*
  - `timelineIndex` : *int*

- **Return Values**:
  - `null` : *null*

---

**APPLY CUE NUMBER ON TIMELINE**

`Pixera.Compound.applyCueNumberOnTimeline`

- **Parameters**:
  - `timelineName` : *string*
  - `cueNumber` : *int*

- **Return Values**:
  - `null` : *null*

---

**APPLY CUE ON TIMELINE**

`Pixera.Compound.applyCueOnTimeline`

- **Parameters**:
  - `timelineName` : *string*
  - `cueName` : *string*

- **Return Values**:
  - `null` : *null*

---

**ADD RESOURCE TO FOLDER**

`Pixera.Compound.addResourceToFolder`

- **Parameters**:
  - `namePath` : *string*
  - `filePath` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**ASSIGN RESOURCE TO LAYER**

`Pixera.Compound.assignResourceToLayer`

- **Parameters**:
  - `resourcePath` : *string*
  - `layerPath` : *string*

- **Return Values**:
  - `null` : *null*

---

**REFRESH RESOURCE**

`Pixera.Compound.refreshResource`

- **Parameters**:
  - `resourcePath` : *string*

- **Return Values**:
  - `null` : *null*

---

**SET TRANSPORT MODE ON LAYER**

`Pixera.Compound.setTransportModeOnLayer`

- **Parameters**:
  - `layerPath` : *string*
  - `mode` : *int*
  - `loop` : *bool*

- **Return Values**:
  - `null` : *null*

---

**GET TRANSPORT MODE ON LAYER**

`Pixera.Compound.getTransportModeOnLayer`

- **Parameters**:
  - `layerPath` : *string*

- **Return Values**:
  - `int` : *int*

---

**GET RESOURCE ASSIGNED TO LAYER**

`Pixera.Compound.getResourceAssignedToLayer`

- **Parameters**:
  - `layerPath` : *string*

- **Return Values**:
  - `string` : *string*

---

**ASSIGN RESOURCE TO CLIP AT TIME BY DMX ID**

`Pixera.Compound.assignResourceToClipAtTimeByDmxId`

- **Parameters**:
  - `layerPath` : *string*
  - `dmxFolderId` : *int*
  - `dmxFileId` : *int*
  - `time` : *double*

- **Return Values**:
  - `null` : *null*

---

**ASSIGN RESOURCE TO CLIP AT HMSFSTRING BY DMX ID**

`Pixera.Compound.assignResourceToClipAtHMSFStringByDmxId`

- **Parameters**:
  - `layerPath` : *string*
  - `dmxFolderId` : *int*
  - `dmxFileId` : *int*
  - `hmsf` : *string*

- **Return Values**:
  - `null` : *null*

---

**ASSIGN RESOURCE TO CLIP AT HMSFBY DMX ID**

`Pixera.Compound.assignResourceToClipAtHMSFByDmxId`

- **Parameters**:
  - `layerPath` : *string*
  - `dmxFolderId` : *int*
  - `dmxFileId` : *int*
  - `h` : *int*
  - `m` : *int*
  - `s` : *int*
  - `f` : *int*

- **Return Values**:
  - `null` : *null*

---

**SET CURRENT TIME OF TIMELINE**

`Pixera.Compound.setCurrentTimeOfTimeline`

- **Parameters**:
  - `timelineName` : *string*
  - `time` : *int*

- **Return Values**:
  - `null` : *null*

---

**SET CURRENT TIME OF TIMELINE IN SECONDS**

`Pixera.Compound.setCurrentTimeOfTimelineInSeconds`

- **Parameters**:
  - `timelineName` : *string*
  - `time` : *double*

- **Return Values**:
  - `null` : *null*

---

**SET CURRENT TIME AND TRANSPORT MODE OF TIMELINE IN SECONDS**

`Pixera.Compound.setCurrentTimeAndTransportModeOfTimelineInSeconds`

- **Parameters**:
  - `timelineName` : *string*
  - `time` : *double*
  - `mode` : *int*

- **Return Values**:
  - `null` : *null*

---

**GET FPS OF TIMELINE**

`Pixera.Compound.getFpsOfTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `double` : *double*

---

**GET CURRENT TIME OF TIMELINE**

`Pixera.Compound.getCurrentTimeOfTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `int` : *int*

---

**GET CURRENT TIME OF TIMELINE IN SECONDS**

`Pixera.Compound.getCurrentTimeOfTimelineInSeconds`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `double` : *double*

---

**GET CURRENT HMSFOF TIMELINE**

`Pixera.Compound.getCurrentHMSFOfTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `string` : *string*

---

**GET CURRENT COUNTDOWN OF TIMELINE**

`Pixera.Compound.getCurrentCountdownOfTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `int` : *int*

---

**GET CURRENT COUNTDOWN HMSFOF TIMELINE**

`Pixera.Compound.getCurrentCountdownHMSFOfTimeline`

- **Parameters**:
  - `timelineName` : *string*

- **Return Values**:
  - `string` : *string*

---

**START OPACITY ANIMATION OF TIMELINE**

`Pixera.Compound.startOpacityAnimationOfTimeline`

- **Parameters**:
  - `timelineName` : *string*
  - `fadeIn` : *bool*
  - `fullFadeDuration` : *double*

- **Return Values**:
  - `null` : *null*

---

**CREATE CLIP ON LAYER AT TIME WITH RESOURCE**

`Pixera.Compound.createClipOnLayerAtTimeWithResource`

- **Parameters**:
  - `layerPath` : *string*
  - `time` : *double*
  - `resourcePath` : *string*

- **Return Values**:
  - `null` : *null*

---

**REMOVE CLIP ON LAYER WITH INDEX**

`Pixera.Compound.removeClipOnLayerWithIndex`

- **Parameters**:
  - `layerPath` : *string*
  - `clipIndex` : *int*

- **Return Values**:
  - `null` : *null*

---

**REMOVE ALL CLIPS ON LAYER**

`Pixera.Compound.removeAllClipsOnLayer`

- **Parameters**:
  - `layerPath` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET CLIP DURATION IN SECONDS WITH INDEX**

`Pixera.Compound.getClipDurationInSecondsWithIndex`

- **Parameters**:
  - `layerPath` : *string*
  - `clipIndex` : *int*

- **Return Values**:
  - `double` : *double*

---

**GET CLIP DURATION IN FRAMES WITH INDEX**

`Pixera.Compound.getClipDurationInFramesWithIndex`

- **Parameters**:
  - `layerPath` : *string*
  - `clipIndex` : *int*

- **Return Values**:
  - `int` : *int*

---

**GET CLIP TIME IN SECONDS WITH INDEX**

`Pixera.Compound.getClipTimeInSecondsWithIndex`

- **Parameters**:
  - `layerPath` : *string*
  - `clipIndex` : *int*

- **Return Values**:
  - `double` : *double*

---

**GET CLIP END TIME IN SECONDS WITH INDEX**

`Pixera.Compound.getClipEndTimeInSecondsWithIndex`

- **Parameters**:
  - `layerPath` : *string*
  - `clipIndex` : *int*

- **Return Values**:
  - `double` : *double*

---

**GET RESOURCE DURATION IN SECONDS**

`Pixera.Compound.getResourceDurationInSeconds`

- **Parameters**:
  - `resourcePath` : *string*

- **Return Values**:
  - `double` : *double*

---

**GET PARAM VALUE**

`Pixera.Compound.getParamValue`

- **Parameters**:
  - `path` : *string*

- **Return Values**:
  - `double` : *double*

---

**SET TIMECODE INPUT**

`Pixera.Compound.setTimecodeInput`

- **Parameters**:
  - `hour` : *int*
  - `minute` : *int*
  - `second` : *int*
  - `frame` : *int*
  - `elapsedTime` : *double*
  - `running` : *bool*
  - `freshMode` : *int*
  - `stateToken` : *int*
  - `format` : *int*

- **Return Values**:
  - `double` : *double*

---

**TAKE OVER ALL CLIENTS**

`Pixera.Compound.takeOverAllClients`

- **Return Values**:
  - `null` : *null*

---

**SET PAUSE SMPTE INPUT**

`Pixera.Compound.setPauseSmpteInput`

- **Parameters**:
  - `doPause` : *bool*

- **Return Values**:
  - `null` : *null*

---

### Session

**CLOSE APP**

`Pixera.Session.closeApp`

- **Parameters**:
  - `saveProject` : *bool*

- **Return Values**:
  - `null` : *null*

---

**LOAD PROJECT**

`Pixera.Session.loadProject`

- **Parameters**:
  - `path` : *string*

- **Return Values**:
  - `null` : *null*

---

**SAVE PROJECT**

`Pixera.Session.saveProject`

- **Return Values**:
  - `null` : *null*

---

**SAVE PROJECT AS**

`Pixera.Session.saveProjectAs`

- **Parameters**:
  - `path` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET PROJECT NAME**

`Pixera.Session.getProjectName`

- **Return Values**:
  - `string` : *string*

---

**SET PROJECT NAME**

`Pixera.Session.setProjectName`

- **Parameters**:
  - `name` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET PROJECT DIRECTORY**

`Pixera.Session.getProjectDirectory`

- **Return Values**:
  - `string` : *string*

---

**GET CONTROL MULTI USER SESSION NAME**

`Pixera.Session.getControlMultiUserSessionName`

- **Return Values**:
  - `string` : *string*

---

**SHUTDOWN SYSTEM**

`Pixera.Session.shutdownSystem`

- **Parameters**:
  - `mode` : *optional<int>*

- **Return Values**:
  - `null` : *null*

---

**GET LIVE SYSTEM IPS**

`Pixera.Session.getLiveSystemIps`

- **Return Values**:
  - `string[]` : *string[]*

---

**GET LIVE SYSTEM STATE**

`Pixera.Session.getLiveSystemState`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `string` : *string*

---

**LIVE SYSTEM STATE CHANGE**

`Pixera.Session.liveSystemStateChange`

- **Parameters**:
  - `ip` : *string*
  - `state` : *string*

- **Return Values**:
  - `null` : *null*

---

**SHUTDOWN LIVE SYSTEM**

`Pixera.Session.shutdownLiveSystem`

- **Parameters**:
  - `ip` : *string*
  - `mode` : *optional<int>*

- **Return Values**:
  - `null` : *null*

---

**WAKE LIVE SYSTEM**

`Pixera.Session.wakeLiveSystem`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `string` : *string*

---

**GET LIVE SYSTEM MAC ADDRESS**

`Pixera.Session.getLiveSystemMacAddress`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `string` : *string*

---

**START LIVE SYSTEM**

`Pixera.Session.startLiveSystem`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `null` : *null*

---

**START LIVE SYSTEMS**

`Pixera.Session.startLiveSystems`

- **Return Values**:
  - `null` : *null*

---

**STOP LIVE SYSTEM**

`Pixera.Session.stopLiveSystem`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `null` : *null*

---

**STOP LIVE SYSTEMS**

`Pixera.Session.stopLiveSystems`

- **Return Values**:
  - `null` : *null*

---

**RESTART LIVE SYSTEM**

`Pixera.Session.restartLiveSystem`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `null` : *null*

---

**RESTART LIVE SYSTEMS**

`Pixera.Session.restartLiveSystems`

- **Return Values**:
  - `null` : *null*

---

**REMOTE SYSTEM STATE CHANGE**

`Pixera.Session.remoteSystemStateChange`

- **Parameters**:
  - `ip` : *string*
  - `state` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET REMOTE SYSTEM IPS**

`Pixera.Session.getRemoteSystemIps`

- **Return Values**:
  - `string[]` : *string[]*

---

**GET REMOTE SYSTEM STATE**

`Pixera.Session.getRemoteSystemState`

- **Parameters**:
  - `ip` : *string*

- **Return Values**:
  - `string` : *string*

---

**SET VIDEO STREAM ACTIVE STATE**

`Pixera.Session.setVideoStreamActiveState`

- **Parameters**:
  - `ip` : *string*
  - `device` : *string*
  - `isActive` : *bool*

- **Return Values**:
  - `null` : *null*

---

**GET VIDEO STREAM ACTIVE STATE**

`Pixera.Session.getVideoStreamActiveState`

- **Parameters**:
  - `ip` : *string*
  - `device` : *string*

- **Return Values**:
  - `bool` : *bool*

---

**GET DEFAULT CLIP DURATIONS AS JSON STRING**

`Pixera.Session.getDefaultClipDurationsAsJsonString`

- **Return Values**:
  - `string` : *string*

---

### LiveSystems

**GET LIVE SYSTEMS**

`Pixera.LiveSystems.getLiveSystems`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**LIVE SYSTEM NOT AVAILABLE**

`Pixera.LiveSystems.liveSystemNotAvailable`

- **Parameters**:
  - `reason` : *int*
  - `system` : *handle*

- **Return Values**:
  - `null` : *null*

---

**GET MULTI USER MEMBERS**

`Pixera.LiveSystems.getMultiUserMembers`

- **Return Values**:
  - `handle[]` : *handle[]*

---

### Settings

### Screens

**GET SCREEN WITH NAME**

`Pixera.Screens.getScreenWithName`

- **Parameters**:
  - `name` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**SET NAMED SCREEN POSITION**

`Pixera.Screens.setNamedScreenPosition`

- **Parameters**:
  - `name` : *string*
  - `xPos` : *optional<double>*
  - `yPos` : *optional<double>*
  - `zPos` : *optional<double>*

- **Return Values**:
  - `null` : *null*

---

**GET SCREENS**

`Pixera.Screens.getScreens`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**GET SCREEN NAMES**

`Pixera.Screens.getScreenNames`

- **Return Values**:
  - `string[]` : *string[]*

---

**GET FIRST TIMELINE WITH HOME SCREEN**

`Pixera.Screens.getFirstTimelineWithHomeScreen`

- **Parameters**:
  - `screenName` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**GET STUDIO CAMERAS**

`Pixera.Screens.getStudioCameras`

- **Return Values**:
  - `handle[]` : *handle[]*

---

### Projectors

**GET PROJECTOR WITH NAME**

`Pixera.Projectors.getProjectorWithName`

- **Parameters**:
  - `name` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**GET PROJECTORS**

`Pixera.Projectors.getProjectors`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**GET PROJECTOR NAMES**

`Pixera.Projectors.getProjectorNames`

- **Return Values**:
  - `string[]` : *string[]*

---

### Resources

**GET RESOURCES**

`Pixera.Resources.getResources`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**GET RESOURCE FOLDER WITH NAME PATH**

`Pixera.Resources.getResourceFolderWithNamePath`

- **Parameters**:
  - `namePath` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**GET RESOURCE FOLDERS**

`Pixera.Resources.getResourceFolders`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**GET TRANSCODING FOLDERS**

`Pixera.Resources.getTranscodingFolders`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**GET JSON DESCRIP**

`Pixera.Resources.getJsonDescrip`

- **Return Values**:
  - `string` : *string*

---

### Timelines

**GET TIMELINE AT INDEX**

`Pixera.Timelines.getTimelineAtIndex`

- **Parameters**:
  - `index` : *int*

- **Return Values**:
  - `handle` : *handle*

---

**GET TIMELINE FROM NAME**

`Pixera.Timelines.getTimelineFromName`

- **Parameters**:
  - `name` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**GET TIMELINES**

`Pixera.Timelines.getTimelines`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**GET TIMELINE NAMES**

`Pixera.Timelines.getTimelineNames`

- **Return Values**:
  - `string[]` : *string[]*

---

**GET TIMELINES SELECTED**

`Pixera.Timelines.getTimelinesSelected`

- **Return Values**:
  - `handle[]` : *handle[]*

---

**CREATE TIMELINE**

`Pixera.Timelines.createTimeline`

- **Return Values**:
  - `handle` : *handle*

---

**GET NODE FROM ID**

`Pixera.Timelines.getNodeFromId`

- **Parameters**:
  - `id` : *double*

- **Return Values**:
  - `handle` : *handle*

---

### Calibration

**SET MARKER POSITIONS**

`Pixera.Calibration.setMarkerPositions`

- **Parameters**:
  - `positions` : *double[]*
  - `markerIds` : *int[]*

- **Return Values**:
  - `null` : *null*

---

### WebViews

**LOAD DEVICE UI**

`Pixera.WebViews.loadDeviceUi`

- **Parameters**:
  - `devicePath` : *string*

- **Return Values**:
  - `null` : *null*

---

**ACTIVATE PREVIOUS FUNC**

`Pixera.WebViews.activatePreviousFunc`

- **Return Values**:
  - `null` : *null*

---

**ACTIVATE NEXT FUNC**

`Pixera.WebViews.activateNextFunc`

- **Return Values**:
  - `null` : *null*

---

**GET LAST ACTIVATED FUNC**

`Pixera.WebViews.getLastActivatedFunc`

- **Return Values**:
  - `string` : *string*

---

**DEVICE ACTIVATED**

`Pixera.WebViews.deviceActivated`

- **Parameters**:
  - `devicePath` : *string*
  - `withSelection` : *bool*

- **Return Values**:
  - `null` : *null*

---

**FUNC ACTIVATED**

`Pixera.WebViews.funcActivated`

- **Parameters**:
  - `funcPath` : *string*
  - `withSelection` : *bool*

- **Return Values**:
  - `null` : *null*

---

**SET FUNC BODY STATE**

`Pixera.WebViews.setFuncBodyState`

- **Parameters**:
  - `funcPath` : *string*
  - `state` : *string*

- **Return Values**:
  - `null` : *null*

---

**GET FUNC BODY STATE**

`Pixera.WebViews.getFuncBodyState`

- **Parameters**:
  - `funcPath` : *string*

- **Return Values**:
  - `string` : *string*

---

**SET TAG**

`Pixera.WebViews.setTag`

- **Parameters**:
  - `tag` : *string*
  - `text` : *string*

- **Return Values**:
  - `null` : *null*

---

**SET EDITOR IS USING BLOCKS**

`Pixera.WebViews.setEditorIsUsingBlocks`

- **Parameters**:
  - `useBlocks` : *bool*

- **Return Values**:
  - `null` : *null*

---

### Ui

**GET COMBO BOX WITH ID**

`Pixera.Ui.getComboBoxWithId`

- **Parameters**:
  - `id` : *double*

- **Return Values**:
  - `handle` : *handle*

---

**SET APP MODE**

`Pixera.Ui.setAppMode`

- **Parameters**:
  - `mode` : *int*

- **Return Values**:
  - `null` : *null*

---

**GET APP MODE**

`Pixera.Ui.getAppMode`

- **Return Values**:
  - `int` : *int*

---

**GET DISPLAY TESTPATTERN**

`Pixera.Ui.getDisplayTestpattern`

- **Return Values**:
  - `bool` : *bool*

---

**SET DISPLAY TESTPATTERN**

`Pixera.Ui.setDisplayTestpattern`

- **Parameters**:
  - `display` : *bool*

- **Return Values**:
  - `null` : *null*

---

**GET PREVIEW CAMERA AS JSON STRING**

`Pixera.Ui.getPreviewCameraAsJsonString`

- **Return Values**:
  - `string` : *string*

---

**SET PREVIEW CAMERA AS JSON STRING**

`Pixera.Ui.setPreviewCameraAsJsonString`

- **Parameters**:
  - `cameraFrustrumStateString` : *string*

- **Return Values**:
  - `null` : *null*

---

**SET DISABLE CONTENT RENDERING**

`Pixera.Ui.setDisableContentRendering`

- **Parameters**:
  - `state` : *bool*

- **Return Values**:
  - `null` : *null*

---

**GET IS CONTENT RENDERING DISABLED**

`Pixera.Ui.getIsContentRenderingDisabled`

- **Return Values**:
  - `bool` : *bool*

---

**SET DISABLE WORKSPACE RENDERING**

`Pixera.Ui.setDisableWorkspaceRendering`

- **Parameters**:
  - `state` : *bool*

- **Return Values**:
  - `null` : *null*

---

**GET IS WORKSPACE RENDERING DISABLED**

`Pixera.Ui.getIsWorkspaceRenderingDisabled`

- **Return Values**:
  - `bool` : *bool*

---

### Direct

**SET REGISTERED**

`Pixera.Direct.setRegistered`

- **Parameters**:
  - `hdls` : *handle[]*
  - `expectedFrequency` : *int*
  - `dampingMs` : *int*
  - `usageHints` : *string[]*

- **Return Values**:
  - `null` : *null*

---

**RELOAD REGISTERED**

`Pixera.Direct.reloadRegistered`

- **Return Values**:
  - `null` : *null*

---

**REGISTER SCREEN**

`Pixera.Direct.registerScreen`

- **Parameters**:
  - `name` : *string*
  - `expectedFrequency` : *int*
  - `dampingMs` : *int*

- **Return Values**:
  - `handle` : *handle*

---

**REGISTER PARAM**

`Pixera.Direct.registerParam`

- **Parameters**:
  - `instancePath` : *string*

- **Return Values**:
  - `handle` : *handle*

---

**REGISTER CAMERA**

`Pixera.Direct.registerCamera`

- **Parameters**:
  - `cameraName` : *string*
  - `expectedFrequency` : *int*

- **Return Values**:
  - `handle` : *handle*

---

**REGISTER PERSPECTIVE**

`Pixera.Direct.registerPerspective`

- **Parameters**:
  - `screenName` : *string*
  - `expectedFrequency` : *int*

- **Return Values**:
  - `handle` : *handle*

---

### Unreal

