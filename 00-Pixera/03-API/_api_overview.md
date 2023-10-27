
# Protocol Overview
This documentation describes revision 349 of the API.

The Pixera API uses the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol.

Pixera API test application by Benni Müller can be found [here](http://www.benni-m.de/index.html#projects).

Descriptions pulled from [pixera_api_examples_rev349.txt](00-Pixera/03-API/docs/pixera_api_examples_rev349.txt)

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

-  All class methods imply a handle parameter in the JSON params object (see examples).
-  Returns the current revision of the API.
-  Release versions have even revision numbers. Beta versions have odd revision numbers.

   - **Return Values**:
     - `int` : *int*

---

**GET HAS FUNCTION**

`Pixera.Utility.getHasFunction`

-  Returns true if the function (or class method) is available.
-  functionName must be the fully qualified name of the function or method,
-  e.g. "Pixera.Screens.Screen.setPosition".

   - **Parameters**:
     - `functionName` : *string*

   - **Return Values**:
     - `bool` : *bool*

---

**OUTPUT DEBUG**

`Pixera.Utility.outputDebug`

-  Outputs a debug string into the Pixera log and returns the same string in
-  the reply.

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

-  Returns the current time in frames. Use getFps() to relate the frames to seconds.

   - **Return Values**:
     - `double` : *double*

---

**GET CURRENT TIME AS STRING**

`Pixera.Utility.getCurrentTimeAsString`

-  Returns the current time as an ISO-8601 string (using the local timezone).

   - **Return Values**:
     - `string` : *string*

---

**NOOP**

`Pixera.Utility.noop`

-  No operation. This function does nothing. It can be used in request/response scenarios
-  (e.g. JSON-RPC) to bookend a set of API invocations. This gives the client a way
-  to know that the last invocation in the set has been processed by Pixera.

   - **Return Values**:
     - `null` : *null*

---

**REQUEST CALLBACK**

`Pixera.Utility.requestCallback`

-  Experimental. Currently only relevant to Javascript interpretation within Pixera.

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

-  See the documentation PDF for more information on monitoring.
-  The Javascript implementation does not support monitoring.
-  In the JSON implementation, the result of this function is a JSON object, not a string.

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

-  In the Control implementation this function is called when monitoring events are sent.

   - **Parameters**:
     - `eventDescription` : *string*

   - **Return Values**:
     - `null` : *null*

---

**SET SHOW CONTEXT IN REPLIES**

`Pixera.Utility.setShowContextInReplies`

-  Only available in json implementation.

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

-  Runs the javascript function jsFunction with code jsCode.

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

-  The Network namespace establishes a bridge between the network connections defined in the API
-  tab and the API entities. E.g. it allows Javascript objects created during use of the API to
-  send data on the connections defined in the API tab.

   - **Parameters**:
     - `conveyorName` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

### Compound

**SET TRANSPORT MODE ON TIMELINE AT INDEX**

`Pixera.Compound.setTransportModeOnTimelineAtIndex`

-  Sets the transport mode of the timeline at the (zero-based) index in
-  the Timelines listing of the Compositing tab.
-  Mode Parameter: Play = 1, Pause = 2, Stop = 3.

   - **Parameters**:
     - `index` : *int*
     - `mode` : *int*

   - **Return Values**:
     - `bool` : *bool*

---

**SET TRANSPORT MODE ON TIMELINE**

`Pixera.Compound.setTransportModeOnTimeline`

-  Sets the transport mode of the timeline identified by its name.
-  Mode Parameter: Play = 1, Pause = 2, Stop = 3.

   - **Parameters**:
     - `timelineName` : *string*
     - `mode` : *int*

   - **Return Values**:
     - `null` : *null*

---

**TOGGLE TRANSPORT**

`Pixera.Compound.toggleTransport`

-  Toggle the timeline between play and pause.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `null` : *null*

---

**GET TRANSPORT MODE ON TIMELINE**

`Pixera.Compound.getTransportModeOnTimeline`

-  Gets the transport mode of the timeline identified by its name.
-  Return values: Play = 1, Pause = 2, Stop = 3.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `int` : *int*

---

**SET OPACITY ON TIMELINE**

`Pixera.Compound.setOpacityOnTimeline`

-  Sets the opacity of the timeline identified by its name.

   - **Parameters**:
     - `timelineName` : *string*
     - `opacity` : *double*

   - **Return Values**:
     - `null` : *null*

---

**GET OPACITY ON TIMELINE**

`Pixera.Compound.getOpacityOnTimeline`

-  Gets the opacity of the timeline identified by its name.

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

-  Set the x position of the first layer of the first timeline.
-  Purely for demonstration, testing purposes.

   - **Parameters**:
     - `val` : *double*

   - **Return Values**:
     - `null` : *null*

---

**SET POS VALUE XY**

`Pixera.Compound.setPosValueXY`

-  Set the x/y position of the first layer of the first timeline.
-  Purely for demonstration, testing purposes.

   - **Parameters**:
     - `valX` : *double*
     - `valY` : *double*

   - **Return Values**:
     - `null` : *null*

---

**SET PARAM VALUE**

`Pixera.Compound.setParamValue`

-  Sets the current value of the parameter.
-  The parameter is identified by a path separated by periods (e.g. "Timeline 1.Layer 1.Opacity").

   - **Parameters**:
     - `path` : *string*
     - `value` : *double*

   - **Return Values**:
     - `null` : *null*

---

**APPLY CUE AT INDEX ON TIMELINE AT INDEX**

`Pixera.Compound.applyCueAtIndexOnTimelineAtIndex`

-  Triggers the cue at the (zero-based) index in the timeline at the (zero-based) index in
-  the Timelines listing of the Compositing tab.

   - **Parameters**:
     - `cueIndex` : *int*
     - `timelineIndex` : *int*

   - **Return Values**:
     - `null` : *null*

---

**APPLY CUE NUMBER ON TIMELINE AT INDEX**

`Pixera.Compound.applyCueNumberOnTimelineAtIndex`

-  Triggers the cue number in the timeline at the (zero-based) index in
-  the Timelines listing of the Compositing tab.

   - **Parameters**:
     - `cueNumber` : *int*
     - `timelineIndex` : *int*

   - **Return Values**:
     - `null` : *null*

---

**APPLY CUE NUMBER ON TIMELINE**

`Pixera.Compound.applyCueNumberOnTimeline`

-  Triggers the cue number in the timeline.

   - **Parameters**:
     - `timelineName` : *string*
     - `cueNumber` : *int*

   - **Return Values**:
     - `null` : *null*

---

**APPLY CUE ON TIMELINE**

`Pixera.Compound.applyCueOnTimeline`

-  Triggers the cue with name in the timeline.

   - **Parameters**:
     - `timelineName` : *string*
     - `cueName` : *string*

   - **Return Values**:
     - `null` : *null*

---

**ADD RESOURCE TO FOLDER**

`Pixera.Compound.addResourceToFolder`

-  Adds the file at the path to the folder with the given name path.

   - **Parameters**:
     - `namePath` : *string*
     - `filePath` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

**ASSIGN RESOURCE TO LAYER**

`Pixera.Compound.assignResourceToLayer`

-  Assigns a resource to a layer. The resource is identified by a path build from signatures and separated by forward slashes
-  (e.g. "Media/Folder/video.mov"). The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `resourcePath` : *string*
     - `layerPath` : *string*

   - **Return Values**:
     - `null` : *null*

---

**REFRESH RESOURCE**

`Pixera.Compound.refreshResource`

-  Refreshes a resource from file. The resource is identified by a path build from signatures and separated by forward slashes
-  (e.g. "Media/Folder/video.mov").

   - **Parameters**:
     - `resourcePath` : *string*

   - **Return Values**:
     - `null` : *null*

---

**SET TRANSPORT MODE ON LAYER**

`Pixera.Compound.setTransportModeOnLayer`

-  Sets the transport mode of a layer: Play = 1, Pause = 2, Stop = 3.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*
     - `mode` : *int*
     - `loop` : *bool*

   - **Return Values**:
     - `null` : *null*

---

**GET TRANSPORT MODE ON LAYER**

`Pixera.Compound.getTransportModeOnLayer`

-  Gets the transport mode of a layer: Play = 1, Pause = 2, Stop = 3.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*

   - **Return Values**:
     - `int` : *int*

---

**GET RESOURCE ASSIGNED TO LAYER**

`Pixera.Compound.getResourceAssignedToLayer`

-  Gets the resource currently assigned to the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").
-  The returned string is the path build from signatures and separated by forward slashes
-  (e.g. "Media/Folder/video.mov").

   - **Parameters**:
     - `layerPath` : *string*

   - **Return Values**:
     - `string` : *string*

---

**ASSIGN RESOURCE TO CLIP AT TIME BY DMX ID**

`Pixera.Compound.assignResourceToClipAtTimeByDmxId`

-  Assign the resource with dmxfolder/dmxfile id to the clip at time in frames by layerpath

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

-  Assign the resource with dmxfolder/dmxfile id to the clip at hmsf time by layerpath

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

-  Assign the resource with dmxfolder/dmxfile id to the clip at h m s f by layerpath

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

-  Sets the current time in frames. Use getFpsOfTimeline() to relate the frames to seconds.

   - **Parameters**:
     - `timelineName` : *string*
     - `time` : *int*

   - **Return Values**:
     - `null` : *null*

---

**SET CURRENT TIME OF TIMELINE IN SECONDS**

`Pixera.Compound.setCurrentTimeOfTimelineInSeconds`

-  Sets the current time in seconds.

   - **Parameters**:
     - `timelineName` : *string*
     - `time` : *double*

   - **Return Values**:
     - `null` : *null*

---

**SET CURRENT TIME AND TRANSPORT MODE OF TIMELINE IN SECONDS**

`Pixera.Compound.setCurrentTimeAndTransportModeOfTimelineInSeconds`

-  Sets the current time in seconds.
-  Mode Parameter: Play = 1, Pause = 2, Stop = 3.

   - **Parameters**:
     - `timelineName` : *string*
     - `time` : *double*
     - `mode` : *int*

   - **Return Values**:
     - `null` : *null*

---

**GET FPS OF TIMELINE**

`Pixera.Compound.getFpsOfTimeline`

-  Gets the frames per second of the timeline.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `double` : *double*

---

**GET CURRENT TIME OF TIMELINE**

`Pixera.Compound.getCurrentTimeOfTimeline`

-  Gets the current time in frames. Use getFpsOfTimeline() to relate the frames to seconds.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `int` : *int*

---

**GET CURRENT TIME OF TIMELINE IN SECONDS**

`Pixera.Compound.getCurrentTimeOfTimelineInSeconds`

-  Gets the current time in seconds.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `double` : *double*

---

**GET CURRENT HMSFOF TIMELINE**

`Pixera.Compound.getCurrentHMSFOfTimeline`

-  Gets the current time as a hours, minutes, seconds, frames string.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `string` : *string*

---

**GET CURRENT COUNTDOWN OF TIMELINE**

`Pixera.Compound.getCurrentCountdownOfTimeline`

-  Gets the current countdown in frames. Use getFpsOfTimeline() to relate the frames to seconds.

   - **Parameters**:
     - `timelineName` : *string*

   - **Return Values**:
     - `int` : *int*

---

**GET CURRENT COUNTDOWN HMSFOF TIMELINE**

`Pixera.Compound.getCurrentCountdownHMSFOfTimeline`

-  Gets the current countdown as a hours, minutes, seconds, frames string.

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

-  Creates a clip at the given time in frames and assigns the resource.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").
-  The resource is identified by a path build from signatures and separated by forward slashes (e.g. "Media/Folder/video.mov").

   - **Parameters**:
     - `layerPath` : *string*
     - `time` : *double*
     - `resourcePath` : *string*

   - **Return Values**:
     - `null` : *null*

---

**REMOVE CLIP ON LAYER WITH INDEX**

`Pixera.Compound.removeClipOnLayerWithIndex`

-  Removes the clip identified by the 0-based clipIndex on the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*
     - `clipIndex` : *int*

   - **Return Values**:
     - `null` : *null*

---

**REMOVE ALL CLIPS ON LAYER**

`Pixera.Compound.removeAllClipsOnLayer`

-  Removes all clips on the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*

   - **Return Values**:
     - `null` : *null*

---

**GET CLIP DURATION IN SECONDS WITH INDEX**

`Pixera.Compound.getClipDurationInSecondsWithIndex`

-  Gets the clip duration in seconds identified by the 0-based clipIndex on the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*
     - `clipIndex` : *int*

   - **Return Values**:
     - `double` : *double*

---

**GET CLIP DURATION IN FRAMES WITH INDEX**

`Pixera.Compound.getClipDurationInFramesWithIndex`

-  Gets the clip duration in frames identified by the 0-based clipIndex on the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*
     - `clipIndex` : *int*

   - **Return Values**:
     - `int` : *int*

---

**GET CLIP TIME IN SECONDS WITH INDEX**

`Pixera.Compound.getClipTimeInSecondsWithIndex`

-  Gets the clip start time in seconds identified by the 0-based clipIndex on the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*
     - `clipIndex` : *int*

   - **Return Values**:
     - `double` : *double*

---

**GET CLIP END TIME IN SECONDS WITH INDEX**

`Pixera.Compound.getClipEndTimeInSecondsWithIndex`

-  Gets the clip end time in seconds identified by the 0-based clipIndex on the layer.
-  The layer is identified by a path separated by periods (e.g. "Timeline 1.Layer 1").

   - **Parameters**:
     - `layerPath` : *string*
     - `clipIndex` : *int*

   - **Return Values**:
     - `double` : *double*

---

**GET RESOURCE DURATION IN SECONDS**

`Pixera.Compound.getResourceDurationInSeconds`

-  Returns the duration of the resource in seconds.
-  The resource is identified by a path build from signatures and separated by forward slashes (e.g. "Media/Folder/video.mov").

   - **Parameters**:
     - `resourcePath` : *string*

   - **Return Values**:
     - `double` : *double*

---

**GET PARAM VALUE**

`Pixera.Compound.getParamValue`

-  Gets the current value of the parameter.
-  The parameter is identified by a path separated by periods (e.g. "Timeline 1.Layer 1.Opacity").

   - **Parameters**:
     - `path` : *string*

   - **Return Values**:
     - `double` : *double*

---

**SET TIMECODE INPUT**

`Pixera.Compound.setTimecodeInput`

-  Set timecode input for midi and artnet timecode.

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

- takeover all clients

   - **Return Values**:
     - `null` : *null*

---

**SET PAUSE SMPTE INPUT**

`Pixera.Compound.setPauseSmpteInput`

- mute all incomming smpte inputs

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

-  Shut down the local machine. There are three options for mode:
-  1: Shut down.
-  2: Shut down and turn off power (if supported).
-  3: Shut down and reboot.
-  Default if no mode is set is 1.

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

-  This function is called in Pixera Control when the live system's state changes.

   - **Parameters**:
     - `ip` : *string*
     - `state` : *string*

   - **Return Values**:
     - `null` : *null*

---

**SHUTDOWN LIVE SYSTEM**

`Pixera.Session.shutdownLiveSystem`

-  Shut down the live system with the given IP. The mode options are the same as for shutdownSystem():
-  Default if no mode is set is 1.

   - **Parameters**:
     - `ip` : *string*
     - `mode` : *optional<int>*

   - **Return Values**:
     - `null` : *null*

---

**WAKE LIVE SYSTEM**

`Pixera.Session.wakeLiveSystem`

-  Wake up the live system that last had the given IP. Uses the MAC address that was last reported
-  for the IP.

   - **Parameters**:
     - `ip` : *string*

   - **Return Values**:
     - `string` : *string*

---

**GET LIVE SYSTEM MAC ADDRESS**

`Pixera.Session.getLiveSystemMacAddress`

-  Returns the last MAC address associated with the live system with the given IP.

   - **Parameters**:
     - `ip` : *string*

   - **Return Values**:
     - `string` : *string*

---

**START LIVE SYSTEM**

`Pixera.Session.startLiveSystem`

-  Start LiveSystem.

   - **Parameters**:
     - `ip` : *string*

   - **Return Values**:
     - `null` : *null*

---

**START LIVE SYSTEMS**

`Pixera.Session.startLiveSystems`

-  Start all LiveSystems in Mapping Live Tab.

   - **Return Values**:
     - `null` : *null*

---

**STOP LIVE SYSTEM**

`Pixera.Session.stopLiveSystem`

-  Start LiveSystem.

   - **Parameters**:
     - `ip` : *string*

   - **Return Values**:
     - `null` : *null*

---

**STOP LIVE SYSTEMS**

`Pixera.Session.stopLiveSystems`

-  Start all LiveSystems in Mapping Live Tab.

   - **Return Values**:
     - `null` : *null*

---

**RESTART LIVE SYSTEM**

`Pixera.Session.restartLiveSystem`

-  Start LiveSystem.

   - **Parameters**:
     - `ip` : *string*

   - **Return Values**:
     - `null` : *null*

---

**RESTART LIVE SYSTEMS**

`Pixera.Session.restartLiveSystems`

-  Start all LiveSystems in Mapping Live Tab.

   - **Return Values**:
     - `null` : *null*

---

**REMOTE SYSTEM STATE CHANGE**

`Pixera.Session.remoteSystemStateChange`

-  This action is run when remote heartbeat tracking detects a state change in the system.

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

-  Get the handles of the live systems.
-  This will also return handles of live systems that are no longer connected.

   - **Return Values**:
     - `handle[]` : *handle[]*

---

**LIVE SYSTEM NOT AVAILABLE**

`Pixera.LiveSystems.liveSystemNotAvailable`

-  Called when the live system has become unavailable.

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

-  Screen name as shown in the inspector.

   - **Parameters**:
     - `name` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

**SET NAMED SCREEN POSITION**

`Pixera.Screens.setNamedScreenPosition`

-  This function was introduced for test purposes, is not typical of the API
-  and is likely to be removed soon. Do not use it in shipping products!
-  The function sets the position of the screen with the given name.
-  The recommended way of doing this is to first use getScreenWithName(.) and
-  then Screen.setPosition(.).

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

-  Returns handles to all screens currently used in the Screens tab.

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

-  Returns handles to all studio cameras currently used in the Screens tab.

   - **Return Values**:
     - `handle[]` : *handle[]*

---

### Projectors

**GET PROJECTOR WITH NAME**

`Pixera.Projectors.getProjectorWithName`

-  Projector name as shown in the inspector.

   - **Parameters**:
     - `name` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

**GET PROJECTORS**

`Pixera.Projectors.getProjectors`

-  Returns handles to all screens currently used in the Mapping tab.

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

-  Returns handles to all the resources that are directly in one folder (i.e. does not consider subfolders).

   - **Return Values**:
     - `handle[]` : *handle[]*

---

**GET RESOURCE FOLDER WITH NAME PATH**

`Pixera.Resources.getResourceFolderWithNamePath`

-  Returns a handle to a folder in the resource tree. The namePath
-  specifies the folder by starting from the root and then listing
-  all the names as seen in the resources tree separated by forward
-  slashes, e.g. "Media/Std Backgrounds/Atmospherics".

   - **Parameters**:
     - `namePath` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

**GET RESOURCE FOLDERS**

`Pixera.Resources.getResourceFolders`

-  Returns the resource folders that are immediate children of this folder.

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

-  Returns the handle of the timeline at the (zero-based) index in
-  the Timelines listing of the Compositing tab.

   - **Parameters**:
     - `index` : *int*

   - **Return Values**:
     - `handle` : *handle*

---

**GET TIMELINE FROM NAME**

`Pixera.Timelines.getTimelineFromName`

-  Returns the handle of the timeline with the given name (as shown in the
-  timeline list).

   - **Parameters**:
     - `name` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

**GET TIMELINES**

`Pixera.Timelines.getTimelines`

-  Returns handles to all timelines.

   - **Return Values**:
     - `handle[]` : *handle[]*

---

**GET TIMELINE NAMES**

`Pixera.Timelines.getTimelineNames`

-  Returns names to all timelines.

   - **Return Values**:
     - `string[]` : *string[]*

---

**GET TIMELINES SELECTED**

`Pixera.Timelines.getTimelinesSelected`

-  Returns handles to all selected timelines

   - **Return Values**:
     - `handle[]` : *handle[]*

---

**CREATE TIMELINE**

`Pixera.Timelines.createTimeline`

-  Create Timeline

   - **Return Values**:
     - `handle` : *handle*

---

**GET NODE FROM ID**

`Pixera.Timelines.getNodeFromId`

-  Returns a handle for the node specified by id after checking that a node with the id exists.
-  Conceptually, the id and the handle are the same but some implementations of the API can not
-  yet consume handles as parameters, making it necessary to translate between the two occasionally.

   - **Parameters**:
     - `id` : *double*

   - **Return Values**:
     - `handle` : *handle*

---

### Calibration

**SET MARKER POSITIONS**

`Pixera.Calibration.setMarkerPositions`

-  Sets the marker positions for projector calibration with external data.
-  Positions must contain the marker coordinates in world space in consecutive order
-  like this: x1, y1, z1, x2, y2, z2, x3, y3, z3, ...
-  markerIds must contain a unique integer id for each marker in the same order as
-  the marker positions. The markerIds matching the coordinates example are 1,2,3.

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

-  Ui namespace is only accessible from plugins hosted in Pixera, i.e. it is
-  not relevant to external API access.

   - **Parameters**:
     - `id` : *double*

   - **Return Values**:
     - `handle` : *handle*

---

**SET APP MODE**

`Pixera.Ui.setAppMode`

-  Set the current AppMode
-  1 = Screens
-  2 = Mapping
-  3 = Compositing
-  4 = Compositing Inside
-  5 = Settings
-  6 = Mapping Screens Feedarea
-  7 = Control

   - **Parameters**:
     - `mode` : *int*

   - **Return Values**:
     - `null` : *null*

---

**GET APP MODE**

`Pixera.Ui.getAppMode`

-  Get the current AppMode

   - **Return Values**:
     - `int` : *int*

---

**GET DISPLAY TESTPATTERN**

`Pixera.Ui.getDisplayTestpattern`

-  Get display Testpattern

   - **Return Values**:
     - `bool` : *bool*

---

**SET DISPLAY TESTPATTERN**

`Pixera.Ui.setDisplayTestpattern`

-  Get display Testpattern

   - **Parameters**:
     - `display` : *bool*

   - **Return Values**:
     - `null` : *null*

---

**GET PREVIEW CAMERA AS JSON STRING**

`Pixera.Ui.getPreviewCameraAsJsonString`

-  Get the current AppMode

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

-  Sets all entities registered in the current thread. Entities that were previously
-  registered that are not in the handle array are removed.
-  usageHints is either empty or it contains one entry for each handle. Possible entries are:
-     "screen"
-     "perspective"
-     "parameter"
-     "studioCamera"

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

-  Updates the representation of all registered entities.

   - **Return Values**:
     - `null` : *null*

---

**REGISTER SCREEN**

`Pixera.Direct.registerScreen`

-  Register the screen for use with the Direct API.

   - **Parameters**:
     - `name` : *string*
     - `expectedFrequency` : *int*
     - `dampingMs` : *int*

   - **Return Values**:
     - `handle` : *handle*

---

**REGISTER PARAM**

`Pixera.Direct.registerParam`

-  Register the parameter for use with the Direct API. At the time when this function is executed
-  the layer should already have been displayed at least once. Otherwise the relevant underlying
-  attributes may not have been initialized yet and can not be cached.
-  The instance path traces the name hierarchy in the timeline tree. E.g. "Timeline 1.Position.x".

   - **Parameters**:
     - `instancePath` : *string*

   - **Return Values**:
     - `handle` : *handle*

---

**REGISTER CAMERA**

`Pixera.Direct.registerCamera`

-  Register the camera with the screen group name for use with the Direct API.

   - **Parameters**:
     - `cameraName` : *string*
     - `expectedFrequency` : *int*

   - **Return Values**:
     - `handle` : *handle*

---

**REGISTER PERSPECTIVE**

`Pixera.Direct.registerPerspective`

-  Register the perspective with the screen name for use with the Direct API.

   - **Parameters**:
     - `screenName` : *string*
     - `expectedFrequency` : *int*

   - **Return Values**:
     - `handle` : *handle*

---

### Unreal

