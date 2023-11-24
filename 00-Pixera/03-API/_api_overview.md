
# Protocol Overview
This documentation describes revision 349 of the API.

The Pixera API uses the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol.

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
## Utility
Syntax: *Pixera.Utility.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getApiRevision` | None | `int`<br> |
| `getHasFunction` | `functionName` : string <br> | `bool`<br> |
| `outputDebug` | `message` : string <br> | `string`<br> |
| `getLicenseJson` | None | `string`<br> |
| `getCurrentTime` | None | `double`<br> |
| `getCurrentTimeAsString` | None | `string`<br> |
| `noop` | None | `null`<br> |
| `requestCallback` | `functionName` : string <br> | `null`<br> |
| `readFileString` | `path` : string <br> | `string`<br> |
| `writeFileString` | `path` : string <br>`fileStr` : string <br> | `null`<br> |
| `getAccessRecipe` | `hdlPath` : string <br> | `string`<br> |
| `pollMonitoring` | None | `string`<br> |
| `unsubscribeMonitoringSubject` | `subject` : string <br> | `bool`<br> |
| `subscribeMonitoringSubject` | `subject` : string <br> | `bool`<br> |
| `setMonitoringEventMode` | `mode` : string <br> | `bool`<br> |
| `monitoringEvent` | `eventDescription` : string <br> | `null`<br> |
| `setShowContextInReplies` | `doShow` : bool <br> | `bool`<br> |
| `setMonitoringHasDelimiter` | `hasDelimiter` : bool <br> | `bool`<br> |
| `runJsScript` | `jsFunction` : string <br>`jsCode` : string <br> | `string`<br> |
| `dynamicRebuildFromJsonDescription` | `deviceName` : string <br>`jsonDescription` : string <br>`folder` : string <br> | `null`<br> |

## Network
Syntax: *Pixera.Network.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getConveyor` | `conveyorName` : string <br> | `handle`<br> |
### Classes
#### Conveyor
Syntax: *Pixera.Network.Conveyor.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Conveyor` | `sendString` | `str` : string <br> | `null`<br> |

## Compound
Syntax: *Pixera.Compound.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `setTransportModeOnTimelineAtIndex` | `index` : int <br>`mode` : int <br> | `bool`<br> |
| `setTransportModeOnTimeline` | `timelineName` : string <br>`mode` : int <br> | `null`<br> |
| `toggleTransport` | `timelineName` : string <br> | `null`<br> |
| `getTransportModeOnTimeline` | `timelineName` : string <br> | `int`<br> |
| `setOpacityOnTimeline` | `timelineName` : string <br>`opacity` : double <br> | `null`<br> |
| `getOpacityOnTimeline` | `timelineName` : string <br> | `double`<br> |
| `startFirstTimeline` | None | `null`<br> |
| `pauseFirstTimeline` | None | `null`<br> |
| `stopFirstTimeline` | None | `null`<br> |
| `setPosValue` | `val` : double <br> | `null`<br> |
| `setPosValueXY` | `valX` : double <br>`valY` : double <br> | `null`<br> |
| `setParamValue` | `path` : string <br>`value` : double <br> | `null`<br> |
| `applyCueAtIndexOnTimelineAtIndex` | `cueIndex` : int <br>`timelineIndex` : int <br> | `null`<br> |
| `applyCueNumberOnTimelineAtIndex` | `cueNumber` : int <br>`timelineIndex` : int <br> | `null`<br> |
| `applyCueNumberOnTimeline` | `timelineName` : string <br>`cueNumber` : int <br> | `null`<br> |
| `applyCueOnTimeline` | `timelineName` : string <br>`cueName` : string <br> | `null`<br> |
| `addResourceToFolder` | `namePath` : string <br>`filePath` : string <br> | `handle`<br> |
| `assignResourceToLayer` | `resourcePath` : string <br>`layerPath` : string <br> | `null`<br> |
| `refreshResource` | `resourcePath` : string <br> | `null`<br> |
| `setTransportModeOnLayer` | `layerPath` : string <br>`mode` : int <br>`loop` : bool <br> | `null`<br> |
| `getTransportModeOnLayer` | `layerPath` : string <br> | `int`<br> |
| `getResourceAssignedToLayer` | `layerPath` : string <br> | `string`<br> |
| `assignResourceToClipAtTimeByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`time` : double <br> | `null`<br> |
| `assignResourceToClipAtHMSFStringByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`hmsf` : string <br> | `null`<br> |
| `assignResourceToClipAtHMSFByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`h` : int <br>`m` : int <br>`s` : int <br>`f` : int <br> | `null`<br> |
| `setCurrentTimeOfTimeline` | `timelineName` : string <br>`time` : int <br> | `null`<br> |
| `setCurrentTimeOfTimelineInSeconds` | `timelineName` : string <br>`time` : double <br> | `null`<br> |
| `setCurrentTimeAndTransportModeOfTimelineInSeconds` | `timelineName` : string <br>`time` : double <br>`mode` : int <br> | `null`<br> |
| `getFpsOfTimeline` | `timelineName` : string <br> | `double`<br> |
| `getCurrentTimeOfTimeline` | `timelineName` : string <br> | `int`<br> |
| `getCurrentTimeOfTimelineInSeconds` | `timelineName` : string <br> | `double`<br> |
| `getCurrentHMSFOfTimeline` | `timelineName` : string <br> | `string`<br> |
| `getCurrentCountdownOfTimeline` | `timelineName` : string <br> | `int`<br> |
| `getCurrentCountdownHMSFOfTimeline` | `timelineName` : string <br> | `string`<br> |
| `startOpacityAnimationOfTimeline` | `timelineName` : string <br>`fadeIn` : bool <br>`fullFadeDuration` : double <br> | `null`<br> |
| `createClipOnLayerAtTimeWithResource` | `layerPath` : string <br>`time` : double <br>`resourcePath` : string <br> | `null`<br> |
| `removeClipOnLayerWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `null`<br> |
| `removeAllClipsOnLayer` | `layerPath` : string <br> | `null`<br> |
| `getClipDurationInSecondsWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `double`<br> |
| `getClipDurationInFramesWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `int`<br> |
| `getClipTimeInSecondsWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `double`<br> |
| `getClipEndTimeInSecondsWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `double`<br> |
| `getResourceDurationInSeconds` | `resourcePath` : string <br> | `double`<br> |
| `getParamValue` | `path` : string <br> | `double`<br> |
| `setTimecodeInput` | `hour` : int <br>`minute` : int <br>`second` : int <br>`frame` : int <br>`elapsedTime` : double <br>`running` : bool <br>`freshMode` : int <br>`stateToken` : int <br>`format` : int <br> | `double`<br> |
| `takeOverAllClients` | None | `null`<br> |
| `setPauseSmpteInput` | `doPause` : bool <br> | `null`<br> |

## Session
Syntax: *Pixera.Session.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `closeApp` | `saveProject` : bool <br> | `null`<br> |
| `loadProject` | `path` : string <br> | `null`<br> |
| `saveProject` | None | `null`<br> |
| `saveProjectAs` | `path` : string <br> | `null`<br> |
| `getProjectName` | None | `string`<br> |
| `setProjectName` | `name` : string <br> | `null`<br> |
| `getProjectDirectory` | None | `string`<br> |
| `getControlMultiUserSessionName` | None | `string`<br> |
| `shutdownSystem` | `mode` : optional<int> <br> | `null`<br> |
| `getLiveSystemIps` | None | `string[]`<br> |
| `getLiveSystemState` | `ip` : string <br> | `string`<br> |
| `liveSystemStateChange` | `ip` : string <br>`state` : string <br> | `null`<br> |
| `shutdownLiveSystem` | `ip` : string <br>`mode` : optional<int> <br> | `null`<br> |
| `wakeLiveSystem` | `ip` : string <br> | `string`<br> |
| `getLiveSystemMacAddress` | `ip` : string <br> | `string`<br> |
| `startLiveSystem` | `ip` : string <br> | `null`<br> |
| `startLiveSystems` | None | `null`<br> |
| `stopLiveSystem` | `ip` : string <br> | `null`<br> |
| `stopLiveSystems` | None | `null`<br> |
| `restartLiveSystem` | `ip` : string <br> | `null`<br> |
| `restartLiveSystems` | None | `null`<br> |
| `remoteSystemStateChange` | `ip` : string <br>`state` : string <br> | `null`<br> |
| `getRemoteSystemIps` | None | `string[]`<br> |
| `getRemoteSystemState` | `ip` : string <br> | `string`<br> |
| `setVideoStreamActiveState` | `ip` : string <br>`device` : string <br>`isActive` : bool <br> | `null`<br> |
| `getVideoStreamActiveState` | `ip` : string <br>`device` : string <br> | `bool`<br> |
| `getDefaultClipDurationsAsJsonString` | None | `string`<br> |

## LiveSystems
Syntax: *Pixera.LiveSystems.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getLiveSystems` | None | `handle[]`<br> |
| `liveSystemNotAvailable` | `reason` : int <br>`system` : handle <br> | `null`<br> |
| `getMultiUserMembers` | None | `handle[]`<br> |
### Classes
#### MultiUserMember
Syntax: *Pixera.LiveSystems.MultiUserMember.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `MultiUserMember` | `getName` | None | `string`<br> |
| `MultiUserMember` | `getIp` | None | `string`<br> |
| `MultiUserMember` | `getState` | None | `string`<br> |
| `MultiUserMember` | `getPerformanceMonitoringValuesJson` | None | `string`<br> |
| `MultiUserMember` | `getPerformanceMonitoringValuesJsonEx` | `filter` : string <br> | `string`<br> |
| `MultiUserMember` | `resetCumulativePerformanceMonitoringValues` | None | `null`<br> |
| `MultiUserMember` | `ensureFileDistribution` | `includeNotUsedYet` : bool <br> | `null`<br> |
| `MultiUserMember` | `shutDown` | `mode` : int <br> | `null`<br> |
| `MultiUserMember` | `wakeUp` | None | `string`<br> |
| `MultiUserMember` | `getMacAddress` | None | `string`<br> |
| `MultiUserMember` | `resetEngine` | None | `null`<br> |
| `MultiUserMember` | `restartEngine` | None | `null`<br> |
| `MultiUserMember` | `startEngine` | None | `null`<br> |
| `MultiUserMember` | `closeEngine` | None | `null`<br> |
| `MultiUserMember` | `triggerBackup` | `applyControlCommand` : optional<bool> <br> | `null`<br> |
| `MultiUserMember` | `getStructureJson` | None | `string`<br> |
| `MultiUserMember` | `getInst` | `instancePath` : string <br> | `handle`<br> |
#### LiveSystem
Syntax: *Pixera.LiveSystems.LiveSystem.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `LiveSystem` | `getName` | None | `string`<br> |
| `LiveSystem` | `getIp` | None | `string`<br> |
| `LiveSystem` | `getState` | None | `string`<br> |
| `LiveSystem` | `setBackupRole` | `role` : int <br> | `null`<br> |
| `LiveSystem` | `getBackupRole` | None | `int`<br> |
| `LiveSystem` | `getPerformanceMonitoringValuesJson` | None | `string`<br> |
| `LiveSystem` | `getPerformanceMonitoringValuesJsonEx` | `filter` : string <br> | `string`<br> |
| `LiveSystem` | `resetCumulativePerformanceMonitoringValues` | None | `null`<br> |
| `LiveSystem` | `moveMappingsToOutputs` | `hdlSrc` : handle <br>`outputIdPathMapStr` : string <br> | `null`<br> |
| `LiveSystem` | `clearExportedMappings` | `path` : string <br>`onlyServicePath` : bool <br> | `null`<br> |
| `LiveSystem` | `exportMappings` | `path` : string <br> | `null`<br> |
| `LiveSystem` | `importMappings` | `path` : string <br>`outputIdPathMapStr` : string <br> | `null`<br> |
| `LiveSystem` | `exportMappingsDirectly` | `path` : string <br> | `null`<br> |
| `LiveSystem` | `importMappingsDirectly` | `path` : string <br>`outputIdPathMapStr` : string <br> | `null`<br> |
| `LiveSystem` | `exportMappingsToLiveSystemPath` | `parentPath` : string <br> | `null`<br> |
| `LiveSystem` | `importMappingsFromLiveSystemPath` | `parentPath` : string <br> | `null`<br> |
| `LiveSystem` | `clearExportedMappingsAtLiveSystemPath` | `path` : string <br> | `null`<br> |
| `LiveSystem` | `ensureFileDistribution` | `includeNotUsedYet` : bool <br> | `null`<br> |
| `LiveSystem` | `shutDown` | `mode` : int <br> | `null`<br> |
| `LiveSystem` | `wakeUp` | None | `string`<br> |
| `LiveSystem` | `getMacAddress` | None | `string`<br> |
| `LiveSystem` | `getGraphicsDevices` | None | `handle[]`<br> |
| `LiveSystem` | `getEnabledOutputs` | None | `handle[]`<br> |
| `LiveSystem` | `getAllOutputs` | None | `handle[]`<br> |
| `LiveSystem` | `getVideoStreamOutputs` | None | `handle[]`<br> |
| `LiveSystem` | `resetEngine` | None | `null`<br> |
| `LiveSystem` | `restartEngine` | None | `null`<br> |
| `LiveSystem` | `startEngine` | None | `null`<br> |
| `LiveSystem` | `closeEngine` | None | `null`<br> |
| `LiveSystem` | `setAudioMasterVolume` | `channel` : int <br>`volume` : double <br> | `null`<br> |
| `LiveSystem` | `getAudioMasterVolume` | `channel` : int <br> | `double`<br> |
| `LiveSystem` | `setAudioMasterMute` | `channel` : int <br>`state` : bool <br> | `null`<br> |
| `LiveSystem` | `getAudioMasterMute` | `channel` : int <br> | `bool`<br> |
| `LiveSystem` | `setAudioTimecodeInput` | `channel` : int <br>`state` : bool <br> | `null`<br> |
| `LiveSystem` | `triggerBackup` | `applyControlCommand` : optional<bool> <br> | `null`<br> |
| `LiveSystem` | `getStructureJson` | None | `string`<br> |
| `LiveSystem` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `LiveSystem` | `getInstancePath` | None | `string`<br> |
#### GraphicsDevice
Syntax: *Pixera.LiveSystems.GraphicsDevice.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `GraphicsDevice` | `getName` | None | `string`<br> |
| `GraphicsDevice` | `getEnabledOutputs` | None | `handle[]`<br> |
| `GraphicsDevice` | `getAllOutputs` | None | `handle[]`<br> |
#### Output
Syntax: *Pixera.LiveSystems.Output.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Output` | `getName` | None | `string`<br> |
| `Output` | `setActive` | `active` : bool <br> | `null`<br> |
| `Output` | `getActive` | None | `bool`<br> |
| `Output` | `setIdentify` | `state` : bool <br> | `null`<br> |
| `Output` | `getIdentify` | None | `bool`<br> |
| `Output` | `getAssignedScreens` | None | `handle[]`<br> |
| `Output` | `getAssignedProjectors` | None | `handle[]`<br> |
| `Output` | `getEnabled` | None | `bool`<br> |
| `Output` | `getForPreview` | None | `bool`<br> |
#### VideoStream
Syntax: *Pixera.LiveSystems.VideoStream.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `VideoStream` | `getName` | None | `string`<br> |
| `VideoStream` | `setActive` | `active` : bool <br> | `null`<br> |
| `VideoStream` | `getActive` | None | `bool`<br> |

## Settings
Syntax: *Pixera.Settings.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getShowDimsInPixels` | None | `bool`<br> |
| `getShowScaleAsSize` | None | `bool`<br> |
| `setFadeToTimeDelay` | `timeInMilliseconds` : int <br> | `null`<br> |
| `getFadeToTimeDelay` | None | `int`<br> |
| `getTranscodingPresets` | None | `string[]`<br> |
| `addOrChangeTranscodingPreset` | `preset` : string <br> | `null`<br> |

## Screens
Syntax: *Pixera.Screens.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getScreenWithName` | `name` : string <br> | `handle`<br> |
| `setNamedScreenPosition` | `name` : string <br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null`<br> |
| `getScreens` | None | `handle[]`<br> |
| `getScreenNames` | None | `string[]`<br> |
| `getFirstTimelineWithHomeScreen` | `screenName` : string <br> | `handle`<br> |
| `getStudioCameras` | None | `handle[]`<br> |
### Classes
#### Screen
Syntax: *Pixera.Screens.Screen.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Screen` | `getId` | None | `double`<br> |
| `Screen` | `getName` | None | `string`<br> |
| `Screen` | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPosition` | None | `ScreenPosValues`<br> |
| `Screen` | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `getRotation` | None | `ScreenPosValues`<br> |
| `Screen` | `setScale` | `xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `bool`<br> |
| `Screen` | `getScale` | None | `ScreenPosValues`<br> |
| `Screen` | `setPosRot` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `setPosRotScale` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPersepective` | None | `handle`<br> |
| `Screen` | `snapPerspectiveCornersToScreen` | `mode` : int <br> | `null`<br> |
| `Screen` | `setPerspectivePosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `setPerspectivePositionWithLookAt` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPerspectivePosition` | None | `ScreenPosValues`<br> |
| `Screen` | `setPerspectiveRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPerspectiveRotation` | None | `ScreenPosValues`<br> |
| `Screen` | `setCameraPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `setCameraPositionWithLookAt` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `getCameraPosition` | None | `ScreenPosValues`<br> |
| `Screen` | `setCameraRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `getCameraRotation` | None | `ScreenPosValues`<br> |
| `Screen` | `setContentSamplingFrustumBase` | `x` : double <br>`y` : double <br>`width` : double <br>`height` : double <br>`rotation` : double <br>`originScreenId` : double <br> | `null`<br> |
| `Screen` | `runCalibration` | `mode` : string <br>`diff` : string <br> | `null`<br> |
| `Screen` | `editCalibration` | `diff` : string <br> | `null`<br> |
| `Screen` | `resetWarpFile` | `diff` : string <br> | `null`<br> |
| `Screen` | `loadWarpFile` | `filePath` : string <br> | `null`<br> |
| `Screen` | `loadWarpFileWithDiff` | `filePath` : string <br>`diff` : string <br> | `null`<br> |
| `Screen` | `addWarpFile` | `filePath` : string <br> | `null`<br> |
| `Screen` | `addWarpFileWithDiff` | `filePath` : string <br>`diff` : string <br> | `null`<br> |
| `Screen` | `loadColorCalibration` | `calibrationName` : string <br> | `null`<br> |
| `Screen` | `runColorCalibration` | None | `null`<br> |
| `Screen` | `setIsVisible` | `isVisible` : bool <br> | `null`<br> |
| `Screen` | `getIsVisible` | None | `bool`<br> |
| `Screen` | `setIsProjectable` | `isProjectable` : bool <br> | `null`<br> |
| `Screen` | `getIsProjectable` | None | `bool`<br> |
| `Screen` | `triggerRefreshMapping` | None | `null`<br> |
| `Screen` | `resetAllColorCorrections` | None | `null`<br> |
| `Screen` | `setColorCorrectionWithPath` | `path` : string <br>`value` : float <br> | `null`<br> |
| `Screen` | `getColorCorrectionWithPath` | `path` : string <br> | `float`<br> |
| `Screen` | `setColorCorrectionAsJsonString` | `colorCorrection` : string <br> | `null`<br> |
| `Screen` | `getColorCorrectionAsJsonString` | None | `string`<br> |
| `Screen` | `getOutput` | None | `handle[]`<br> |
| `Screen` | `setBlackout` | `isActive` : bool <br> | `null`<br> |
| `Screen` | `getBlackout` | None | `bool`<br> |
| `Screen` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Screen` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Screen` | `getInstancePath` | None | `string`<br> |
#### StudioCamera
Syntax: *Pixera.Screens.StudioCamera.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `StudioCamera` | `getName` | None | `string`<br> |
| `StudioCamera` | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null`<br> |
| `StudioCamera` | `getPosition` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `double[]`<br> |
| `StudioCamera` | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null`<br> |
| `StudioCamera` | `getRotation` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `double[]`<br> |
| `StudioCamera` | `setTransformation` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`fov` : optional<double> <br>`aspectRatio` : optional<double> <br> | `null`<br> |
| `StudioCamera` | `setTransformationAndLensProps` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null`<br> |
| `StudioCamera` | `setTransformationAndLensPropsExt` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`focalDistance` : double <br>`zoom` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`k3` : double <br>`p1` : double <br>`p2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br>`overscan` : double <br> | `null`<br> |
| `StudioCamera` | `setTrackingInputPause` | `pause` : bool <br> | `null`<br> |
| `StudioCamera` | `getTrackingInputPause` | None | `bool`<br> |
| `StudioCamera` | `setUsePositionPropertiesFromTracking` | `pause` : bool <br> | `null`<br> |
| `StudioCamera` | `getUsePositionPropertiesFromTracking` | None | `bool`<br> |
| `StudioCamera` | `setUseRotationPropertiesFromTracking` | `pause` : bool <br> | `null`<br> |
| `StudioCamera` | `getUseRotationPropertiesFromTracking` | None | `bool`<br> |
| `StudioCamera` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `StudioCamera` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `StudioCamera` | `getInstancePath` | None | `string`<br> |
#### Perspective
Syntax: *Pixera.Screens.Perspective.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Perspective` | `getName` | None | `string`<br> |
| `Perspective` | `setTransformation` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`fov` : optional<double> <br>`aspectRatio` : optional<double> <br> | `null`<br> |
| `Perspective` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Perspective` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Perspective` | `getInstancePath` | None | `string`<br> |

## Projectors
Syntax: *Pixera.Projectors.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getProjectorWithName` | `name` : string <br> | `handle`<br> |
| `getProjectors` | None | `handle[]`<br> |
| `getProjectorNames` | None | `string[]`<br> |
### Classes
#### Projector
Syntax: *Pixera.Projectors.Projector.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Projector` | `getPosition` | None | `ProjectorPosValues`<br> |
| `Projector` | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Projector` | `getRotation` | None | `ProjectorPosValues`<br> |
| `Projector` | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Projector` | `getName` | None | `string`<br> |
| `Projector` | `activateScreenMapping` | `screenId` : double <br>`isActive` : bool <br> | `null`<br> |
| `Projector` | `setBlackout` | `isActive` : bool <br> | `null`<br> |
| `Projector` | `getBlackout` | None | `bool`<br> |
| `Projector` | `setSoftedgeVisible` | `screenName` : string <br>`visible` : bool <br> | `null`<br> |
| `Projector` | `resetAllColorCorrections` | None | `null`<br> |
| `Projector` | `setColorCorrectionWithPath` | `path` : string <br>`value` : float <br> | `null`<br> |
| `Projector` | `getColorCorrectionWithPath` | `path` : string <br> | `float`<br> |
| `Projector` | `setColorCorrectionAsJsonString` | `colorCorrection` : string <br> | `null`<br> |
| `Projector` | `getColorCorrectionAsJsonString` | None | `string`<br> |
| `Projector` | `getOutput` | None | `handle`<br> |
| `Projector` | `setOutput` | `outputHandle` : handle <br> | `null`<br> |
| `Projector` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Projector` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Projector` | `getInstancePath` | None | `string`<br> |

## Resources
Syntax: *Pixera.Resources.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getResources` | None | `handle[]`<br> |
| `getResourceFolderWithNamePath` | `namePath` : string <br> | `handle`<br> |
| `getResourceFolders` | None | `handle[]`<br> |
| `getTranscodingFolders` | None | `handle[]`<br> |
| `getJsonDescrip` | None | `string`<br> |
### Classes
#### ResourceFolder
Syntax: *Pixera.Resources.ResourceFolder.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `ResourceFolder` | `ref` | None | `handle`<br> |
| `ResourceFolder` | `getName` | None | `string`<br> |
| `ResourceFolder` | `setName` | `name` : string <br> | `null`<br> |
| `ResourceFolder` | `getResourceFolders` | None | `handle[]`<br> |
| `ResourceFolder` | `getResources` | None | `handle[]`<br> |
| `ResourceFolder` | `getResourceAtIndex` | `index` : int <br> | `handle`<br> |
| `ResourceFolder` | `addResource` | `path` : string <br> | `handle`<br> |
| `ResourceFolder` | `addResourcesFromDirectory` | `path` : string <br>`removeOthers` : bool <br>`checkRedundancy` : bool <br> | `handle[]`<br> |
| `ResourceFolder` | `addResourcesFromDirectoryRemoveAssets` | `path` : string <br>`removeOthers` : bool <br>`checkRedundancy` : bool <br> | `handle[]`<br> |
| `ResourceFolder` | `addInternalResource` | `signature` : string <br>`resKind` : int <br> | `handle`<br> |
| `ResourceFolder` | `createFoldersFrom` | `path` : string <br> | `null`<br> |
| `ResourceFolder` | `refreshResources` | None | `null`<br> |
| `ResourceFolder` | `moveResourceToThis` | `id` : double <br> | `null`<br> |
| `ResourceFolder` | `removeThis` | None | `null`<br> |
| `ResourceFolder` | `removeThisIncludingAssets` | None | `null`<br> |
| `ResourceFolder` | `removeAllContents` | None | `null`<br> |
| `ResourceFolder` | `removeAllContentsIncludingAssets` | None | `null`<br> |
| `ResourceFolder` | `deleteAllContentsAssetsFromLiveSystem` | `apEntityLiveSystemHandle` : handle <br> | `null`<br> |
| `ResourceFolder` | `resetDistributionTargets` | None | `null`<br> |
| `ResourceFolder` | `changeDistributionTarget` | `apEntityLiveSystemHandle` : handle <br>`shouldDistribute` : bool <br> | `null`<br> |
| `ResourceFolder` | `replaceResourcesByString` | `searchString` : string <br>`replaceString` : string <br>`path` : string <br> | `null`<br> |
| `ResourceFolder` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `ResourceFolder` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `ResourceFolder` | `getInstancePath` | None | `string`<br> |
| `ResourceFolder` | `getDmxId` | None | `int`<br> |
| `ResourceFolder` | `getCombinedDmxId` | None | `int`<br> |
| `ResourceFolder` | `setDmxId` | `id` : int <br> | `null`<br> |
#### TranscodingFolder
Syntax: *Pixera.Resources.TranscodingFolder.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `TranscodingFolder` | `getUsedTranscodingPreset` | None | `string`<br> |
| `TranscodingFolder` | `setUsedTranscodingPreset` | `preset` : string <br> | `null`<br> |
| `TranscodingFolder` | `getTranscodeAutomatically` | None | `bool`<br> |
| `TranscodingFolder` | `setTranscodeAutomatically` | `autoTranscode` : bool <br> | `null`<br> |
| `TranscodingFolder` | `getUseRxCacheAsDestination` | None | `bool`<br> |
| `TranscodingFolder` | `setRxCacheAsDestination` | `useRxCache` : bool <br> | `null`<br> |
| `TranscodingFolder` | `getDestinationDirectory` | None | `string`<br> |
| `TranscodingFolder` | `setDestinationDirectory` | `path` : string <br> | `null`<br> |
#### Resource
Syntax: *Pixera.Resources.Resource.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Resource` | `ref` | None | `handle`<br> |
| `Resource` | `removeThis` | None | `null`<br> |
| `Resource` | `deleteFilesOnSystems` | None | `null`<br> |
| `Resource` | `removeThisIncludingAssets` | None | `null`<br> |
| `Resource` | `deleteAssetFromLiveSystem` | `apEntityLiveSystemHandle` : handle <br> | `null`<br> |
| `Resource` | `resetDistributionTargets` | None | `null`<br> |
| `Resource` | `changeDistributionTarget` | `apEntityLiveSystemHandle` : handle <br>`shouldDistribute` : bool <br> | `null`<br> |
| `Resource` | `getName` | None | `string`<br> |
| `Resource` | `setName` | `name` : string <br> | `null`<br> |
| `Resource` | `getFps` | None | `double`<br> |
| `Resource` | `getResolution` | None | `double[]`<br> |
| `Resource` | `getIsActive` | None | `bool`<br> |
| `Resource` | `getVideoStreamModes` | None | `string[]`<br> |
| `Resource` | `setVideoStreamMode` | `index` : int <br> | `null`<br> |
| `Resource` | `getId` | None | `double`<br> |
| `Resource` | `getDuration` | None | `double`<br> |
| `Resource` | `getType` | None | `string`<br> |
| `Resource` | `setCurrentVersion` | `version` : string <br> | `null`<br> |
| `Resource` | `getCurrentVersion` | None | `string`<br> |
| `Resource` | `getVersions` | None | `string[]`<br> |
| `Resource` | `getVersionSuffix` | None | `string[]`<br> |
| `Resource` | `rescanVersions` | None | `null`<br> |
| `Resource` | `getThumbnailAsBase64` | None | `string`<br> |
| `Resource` | `getHasPendingTransfer` | None | `bool`<br> |
| `Resource` | `getIsInUse` | None | `double`<br> |
| `Resource` | `getLastUsageBeginTime` | None | `double`<br> |
| `Resource` | `getLastUsageBeginTimeAsString` | None | `string`<br> |
| `Resource` | `getLastUsageEndTime` | None | `double`<br> |
| `Resource` | `getLastUsageEndTimeAsString` | None | `string`<br> |
| `Resource` | `getFilePath` | None | `string`<br> |
| `Resource` | `setText` | `text` : string <br> | `null`<br> |
| `Resource` | `getText` | None | `string`<br> |
| `Resource` | `setFontWithName` | `fontName` : string <br> | `bool`<br> |
| `Resource` | `getFontName` | None | `string`<br> |
| `Resource` | `setFontWithPath` | `fontPath` : string <br> | `bool`<br> |
| `Resource` | `setHorizontalTextAlignment` | `textAlignment` : int <br> | `bool`<br> |
| `Resource` | `getHorizontalTextAlignment` | None | `int`<br> |
| `Resource` | `setVerticalTextAlignment` | `textAlignment` : int <br> | `bool`<br> |
| `Resource` | `getVerticalTextAlignment` | None | `int`<br> |
| `Resource` | `setLineHeight` | `lineHeight` : double <br> | `bool`<br> |
| `Resource` | `getLineHeight` | None | `double`<br> |
| `Resource` | `getTextMeasurementsWidthAndHeight` | None | `int[]`<br> |
| `Resource` | `setUrl` | `url` : string <br> | `null`<br> |
| `Resource` | `getUrl` | None | `string`<br> |
| `Resource` | `setColorTransformPath` | `colorTransformPath` : string <br> | `null`<br> |
| `Resource` | `getColorTransformPath` | None | `string`<br> |
| `Resource` | `clearColorTransformPath` | None | `null`<br> |
| `Resource` | `refresh` | `text` : string <br> | `null`<br> |
| `Resource` | `distribute` | None | `null`<br> |
| `Resource` | `getDmxId` | None | `int`<br> |
| `Resource` | `setDmxId` | `id` : int <br> | `null`<br> |
| `Resource` | `removeMultiresourceIndex` | `index` : int <br> | `null`<br> |
| `Resource` | `addMultiresourceItem` | `id` : double <br> | `null`<br> |
| `Resource` | `getMultiresourceItems` | None | `handle[]`<br> |
| `Resource` | `replaceMultiresourceItemByIndex` | `index` : int <br>`id` : double <br> | `null`<br> |
| `Resource` | `setMultiresourceResolution` | `width` : int <br>`height` : int <br> | `null`<br> |
| `Resource` | `setMultiresourceItemSizebyIndex` | `index` : int <br>`width` : double <br>`height` : double <br> | `null`<br> |
| `Resource` | `setMultiresourceItemPositionbyIndex` | `index` : int <br>`x` : double <br>`y` : double <br> | `null`<br> |
| `Resource` | `setUseGradient` | `useGradient` : bool <br> | `null`<br> |
| `Resource` | `getUseGradient` | None | `bool`<br> |
| `Resource` | `setColors` | `argbCols` : uint[] <br>`positions` : double[] <br>`colNames` : string[] <br>`useGradient` : optional<bool> <br> | `null`<br> |
| `Resource` | `setColorAtIndex` | `index` : int <br>`red` : int <br>`green` : int <br>`blue` : int <br>`alpha` : int <br>`position` : double <br>`name` : string <br>`useGradient` : optional<bool> <br> | `null`<br> |
| `Resource` | `getColorAtIndex` | `colorIndex` : int <br> | `int`<br> |
| `Resource` | `getColorPositionAtIndex` | `colorIndex` : int <br> | `double`<br> |
| `Resource` | `launchVirtualWorld` | `action` : string <br> | `null`<br> |
| `Resource` | `getUnrealWorld` | None | `handle`<br> |
| `Resource` | `setMultiResourceItemRestrictedServiceIps` | `itemIndex` : int <br>`ipAdresses` : string[] <br> | `null`<br> |
| `Resource` | `getMultiResourceItemRestrictedServiceIps` | `itemIndex` : int <br> | `string[]`<br> |
| `Resource` | `replace` | `path` : string <br> | `null`<br> |
| `Resource` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Resource` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Resource` | `getInstancePath` | None | `string`<br> |
| `Resource` | `transcodeWithExisitngPreset` | `presetName` : string <br>`useRxCache` : bool <br>`destinationPath` : string <br>`startFrame` : int <br>`endFrame` : int <br>`serviceId` : uint <br> | `null`<br> |
| `Resource` | `transcodeWithSettings` | `settings` : string <br>`useRxCache` : bool <br>`destinationPath` : string <br>`startFrame` : int <br>`endFrame` : int <br>`serviceId` : uint <br> | `null`<br> |
| `Resource` | `moveToTranscodingFolder` | `folderPath` : string <br> | `null`<br> |
#### UnrealWorld
Syntax: *Pixera.Resources.UnrealWorld.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `UnrealWorld` | `getLevelNames` | None | `string[]`<br> |
| `UnrealWorld` | `loadLevel` | `levelName` : string <br> | `null`<br> |
| `UnrealWorld` | `getEventTriggerNames` | None | `string[]`<br> |
| `UnrealWorld` | `triggerEventByName` | `triggerName` : string <br> | `null`<br> |
| `UnrealWorld` | `createNDisplayConfig` | None | `null`<br> |
| `UnrealWorld` | `runUnreal` | None | `null`<br> |
| `UnrealWorld` | `killUnreal` | None | `null`<br> |
| `UnrealWorld` | `getName` | None | `string`<br> |
| `UnrealWorld` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `UnrealWorld` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `UnrealWorld` | `getInstancePath` | None | `string`<br> |

## Timelines
Syntax: *Pixera.Timelines.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getTimelineAtIndex` | `index` : int <br> | `handle`<br> |
| `getTimelineFromName` | `name` : string <br> | `handle`<br> |
| `getTimelines` | None | `handle[]`<br> |
| `getTimelineNames` | None | `string[]`<br> |
| `getTimelinesSelected` | None | `handle[]`<br> |
| `createTimeline` | None | `handle`<br> |
| `getNodeFromId` | `id` : double <br> | `handle`<br> |
### Classes
#### Timeline
Syntax: *Pixera.Timelines.Timeline.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Timeline` | `ref` | None | `handle`<br> |
| `Timeline` | `removeThis` | None | `null`<br> |
| `Timeline` | `duplicateThis` | `withoutClipsCues` : optional<bool> <br> | `handle`<br> |
| `Timeline` | `selectThis` | None | `null`<br> |
| `Timeline` | `getZoomFactor` | None | `double`<br> |
| `Timeline` | `setZoomFactor` | `zoomFactor` : double <br> | `null`<br> |
| `Timeline` | `getVerticalScrollOffset` | None | `int`<br> |
| `Timeline` | `setVerticalScrollOffset` | `offset` : int <br> | `null`<br> |
| `Timeline` | `getHorizontalScrollOffset` | None | `int`<br> |
| `Timeline` | `setHorizontalScrollOffset` | `offset` : int <br> | `null`<br> |
| `Timeline` | `moveInRenderOrder` | `moveDown` : bool <br> | `null`<br> |
| `Timeline` | `getLayers` | None | `handle[]`<br> |
| `Timeline` | `getLayerNames` | None | `string[]`<br> |
| `Timeline` | `getLayersSelected` | None | `handle[]`<br> |
| `Timeline` | `selectLayerByIndex` | `index` : int <br> | `null`<br> |
| `Timeline` | `selectLayerByNames` | `layerNames` : string[] <br> | `null`<br> |
| `Timeline` | `getLayerAtIndex` | `index` : int <br> | `handle`<br> |
| `Timeline` | `createLayer` | None | `handle`<br> |
| `Timeline` | `getCueInfosAsJsonString` | None | `string`<br> |
| `Timeline` | `getCues` | None | `handle[]`<br> |
| `Timeline` | `getCueNames` | None | `string[]`<br> |
| `Timeline` | `getCueAtIndex` | `index` : int <br> | `handle`<br> |
| `Timeline` | `getCueFromName` | `name` : string <br> | `handle`<br> |
| `Timeline` | `getCueFromNumber` | `number` : int <br> | `handle`<br> |
| `Timeline` | `applyCueWithName` | `name` : string <br> | `null`<br> |
| `Timeline` | `applyCueWithNumber` | `number` : int <br> | `null`<br> |
| `Timeline` | `createCue` | `name` : string <br>`timeInFrames` : double <br>`operation` : int <br> | `handle`<br> |
| `Timeline` | `removeCues` | None | `null`<br> |
| `Timeline` | `createPauseCueBeforeSelectedClips` | None | `null`<br> |
| `Timeline` | `play` | None | `null`<br> |
| `Timeline` | `pause` | None | `null`<br> |
| `Timeline` | `stop` | None | `null`<br> |
| `Timeline` | `toggleTransport` | None | `null`<br> |
| `Timeline` | `store` | None | `null`<br> |
| `Timeline` | `reset` | None | `null`<br> |
| `Timeline` | `getAttributes` | None | `TimelineAttributes`<br> |
| `Timeline` | `setCurrentFrame` | `time` : int <br> | `bool`<br> |
| `Timeline` | `setCurrentTime` | `time` : int <br> | `null`<br> |
| `Timeline` | `getCurrentTime` | None | `int`<br> |
| `Timeline` | `scrubCurrentTime` | `frames` : int <br> | `null`<br> |
| `Timeline` | `CurrentTime` | `time` : int <br>`doSet` : bool <br> | `int`<br> |
| `Timeline` | `getCurrentHMSF` | None | `string`<br> |
| `Timeline` | `setTransportMode` | `mode` : int <br> | `bool`<br> |
| `Timeline` | `getTransportMode` | None | `int`<br> |
| `Timeline` | `setTimecodeInput` | `hour` : int <br>`minute` : int <br>`second` : int <br>`frame` : int <br>`elapsedTime` : double <br>`running` : bool <br>`freshMode` : int <br>`stateToken` : int <br>`format` : int <br> | `double`<br> |
| `Timeline` | `getFps` | None | `double`<br> |
| `Timeline` | `getName` | None | `string`<br> |
| `Timeline` | `setName` | `name` : string <br> | `null`<br> |
| `Timeline` | `moveToNextCue` | None | `null`<br> |
| `Timeline` | `moveToNextCueIgnoreProperties` | None | `null`<br> |
| `Timeline` | `getCueNext` | None | `handle`<br> |
| `Timeline` | `moveToPreviousCue` | None | `null`<br> |
| `Timeline` | `moveToPreviousCueIgnoreProperties` | None | `null`<br> |
| `Timeline` | `getCuePrevious` | None | `handle`<br> |
| `Timeline` | `ignoreNextCue` | None | `null`<br> |
| `Timeline` | `ignoreNextCueWithOperation` | `cueOperation` : int <br> | `null`<br> |
| `Timeline` | `blendToTime` | `goalTime` : double <br>`blendDuration` : double <br>`preloadDelayInMilliseconds` : optional<int> <br> | `null`<br> |
| `Timeline` | `blendToTimeWithTransportMode` | `goalTime` : double <br>`blendDuration` : double <br>`transportMode` : int <br>`preloadDelayInMilliseconds` : optional<int> <br> | `null`<br> |
| `Timeline` | `setBlendToTimeMode` | `mode` : int <br> | `bool`<br> |
| `Timeline` | `setSpeedFactor` | `factor` : double <br> | `null`<br> |
| `Timeline` | `getSpeedFactor` | None | `double`<br> |
| `Timeline` | `setOpacity` | `value` : double <br> | `null`<br> |
| `Timeline` | `getOpacity` | None | `double`<br> |
| `Timeline` | `startOpacityAnimation` | `fadeIn` : bool <br>`durationFrames` : double <br> | `null`<br> |
| `Timeline` | `setSmpteMode` | `mode` : int <br> | `null`<br> |
| `Timeline` | `getSmpteMode` | None | `int`<br> |
| `Timeline` | `storeRecordedValues` | None | `null`<br> |
| `Timeline` | `setSmpteInputBehaviour` | `mode` : int <br> | `null`<br> |
| `Timeline` | `getSmpteInputBehaviour` | None | `int`<br> |
| `Timeline` | `setSmpteOffset` | `time` : double <br> | `null`<br> |
| `Timeline` | `getSmpteOffset` | None | `double`<br> |
| `Timeline` | `resetRecordedValues` | None | `null`<br> |
| `Timeline` | `getTimelineInfosAsJsonString` | None | `string`<br> |
| `Timeline` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Timeline` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Timeline` | `getInstancePath` | None | `string`<br> |
#### Layer
Syntax: *Pixera.Timelines.Layer.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Layer` | `ref` | None | `handle`<br> |
| `Layer` | `removeThis` | None | `null`<br> |
| `Layer` | `getNodes` | None | `handle[]`<br> |
| `Layer` | `getNodeWithName` | `name` : string <br> | `handle`<br> |
| `Layer` | `getParamWithName` | `name` : string <br> | `handle`<br> |
| `Layer` | `getSpatialParametersAtTime` | `time` : double <br> | `double[]`<br> |
| `Layer` | `getTimeline` | None | `handle`<br> |
| `Layer` | `setName` | `name` : string <br> | `null`<br> |
| `Layer` | `getName` | None | `string`<br> |
| `Layer` | `resetLayer` | None | `null`<br> |
| `Layer` | `getLayerJsonDescrip` | None | `string`<br> |
| `Layer` | `setLayerJsonDescrip` | `descrip` : string <br>`makeAllDominant` : bool <br> | `null`<br> |
| `Layer` | `getJsonDescrip` | None | `string`<br> |
| `Layer` | `initFromJsonDescrip` | `descrip` : string <br> | `null`<br> |
| `Layer` | `setOpacity` | `value` : double <br> | `null`<br> |
| `Layer` | `getOpacity` | None | `double`<br> |
| `Layer` | `resetOpacity` | None | `null`<br> |
| `Layer` | `setVolume` | `value` : double <br> | `null`<br> |
| `Layer` | `getVolume` | None | `double`<br> |
| `Layer` | `resetVolume` | None | `null`<br> |
| `Layer` | `muteLayer` | None | `null`<br> |
| `Layer` | `unMuteLayer` | None | `null`<br> |
| `Layer` | `getIsLayerMuted` | None | `bool`<br> |
| `Layer` | `muteAudio` | None | `null`<br> |
| `Layer` | `unMuteAudio` | None | `null`<br> |
| `Layer` | `getIsAudioMuted` | None | `bool`<br> |
| `Layer` | `getDmxMuteState` | None | `int`<br> |
| `Layer` | `setDmxMuteState` | `muteState` : uint <br> | `null`<br> |
| `Layer` | `toggleExplicitMute` | `flag` : uint <br> | `null`<br> |
| `Layer` | `setTransport` | `mode` : int <br>`loop` : bool <br> | `null`<br> |
| `Layer` | `getTransportMode` | None | `int`<br> |
| `Layer` | `resetTransportMode` | None | `null`<br> |
| `Layer` | `getTransportLoop` | None | `bool`<br> |
| `Layer` | `assignResource` | `id` : double <br> | `null`<br> |
| `Layer` | `assignResourceWithFade` | `id` : double <br>`fadeDuration` : double <br> | `null`<br> |
| `Layer` | `getAssignedResource` | None | `handle`<br> |
| `Layer` | `resetAssignedResource` | None | `null`<br> |
| `Layer` | `getAssignedModelResource` | None | `handle`<br> |
| `Layer` | `resetAssignedModelResource` | None | `null`<br> |
| `Layer` | `getFxNames` | None | `string[]`<br> |
| `Layer` | `setFadeDurationDominantResourceChange` | `value` : double <br> | `null`<br> |
| `Layer` | `getFadeDurationDominantResourceChange` | None | `double`<br> |
| `Layer` | `createClip` | None | `handle`<br> |
| `Layer` | `createClipAtTime` | `timeInFrames` : double <br> | `handle`<br> |
| `Layer` | `controlClipBorder` | `clip` : handle <br>`isEnter` : bool <br>`isIncremental` : bool <br>`entryTime` : double <br> | `null`<br> |
| `Layer` | `getClipAtIndex` | `index` : int <br> | `handle`<br> |
| `Layer` | `getClips` | None | `handle[]`<br> |
| `Layer` | `getClipCurrent` | `offset` : int <br> | `handle`<br> |
| `Layer` | `getClipsSelected` | None | `handle[]`<br> |
| `Layer` | `removeClips` | None | `null`<br> |
| `Layer` | `setHomeScreenFromScreenName` | `screenName` : string <br> | `null`<br> |
| `Layer` | `getHomeScreenName` | None | `string`<br> |
| `Layer` | `setBlendMode` | `blendMode` : string <br> | `null`<br> |
| `Layer` | `getBlendMode` | None | `string`<br> |
| `Layer` | `addEffectById` | `id` : double <br> | `null`<br> |
| `Layer` | `setPreloadPermanently` | `doPreloadPermanently` : bool <br> | `null`<br> |
| `Layer` | `getPreloadPermanently` | None | `bool`<br> |
| `Layer` | `setRestrictToServiceWithIps` | `doRestrict` : bool <br>`ipAdresses` : string[] <br> | `null`<br> |
| `Layer` | `getRestrictToService` | None | `bool`<br> |
| `Layer` | `getRestrictedServiceIps` | None | `string[]`<br> |
| `Layer` | `getOffsets` | None | `double[]`<br> |
| `Layer` | `setOffsets` | `x` : optional<double> <br>`y` : optional<double> <br>`z` : optional<double> <br>`xr` : optional<double> <br>`yr` : optional<double> <br>`zr` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `null`<br> |
| `Layer` | `setCurrentValuesToOffset` | `typeIndex` : int <br>`resetDominant` : optional<bool> <br>`removeKeyframesClips` : optional<bool> <br> | `null`<br> |
| `Layer` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Layer` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Layer` | `getInstancePath` | None | `string`<br> |
#### Clip
Syntax: *Pixera.Timelines.Clip.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Clip` | `getId` | None | `double`<br> |
| `Clip` | `removeThis` | None | `null`<br> |
| `Clip` | `getTimeline` | None | `handle`<br> |
| `Clip` | `setTime` | `time` : double <br> | `null`<br> |
| `Clip` | `getTime` | None | `double`<br> |
| `Clip` | `setDuration` | `duration` : double <br> | `null`<br> |
| `Clip` | `getDuration` | None | `double`<br> |
| `Clip` | `setLabel` | `label` : string <br> | `null`<br> |
| `Clip` | `getLabel` | None | `string`<br> |
| `Clip` | `getPlayMode` | None | `int`<br> |
| `Clip` | `setPlayMode` | `playMode` : int <br> | `null`<br> |
| `Clip` | `getSpeed` | None | `double`<br> |
| `Clip` | `setSpeed` | `speed` : double <br> | `null`<br> |
| `Clip` | `getBlendFrames` | None | `bool`<br> |
| `Clip` | `setBlendFrames` | `doFrameblending` : bool <br> | `null`<br> |
| `Clip` | `getInpoint` | None | `double`<br> |
| `Clip` | `setInpoint` | `inpoint` : double <br> | `null`<br> |
| `Clip` | `getOutpoint` | None | `double`<br> |
| `Clip` | `setOutpoint` | `inpoint` : double <br> | `null`<br> |
| `Clip` | `assignResource` | `resId` : double <br>`setToResourceDuration` : optional<bool> <br> | `null`<br> |
| `Clip` | `getAssignedResource` | None | `handle`<br> |
| `Clip` | `setToResourceDuration` | None | `null`<br> |
| `Clip` | `createEvent` | `namePath` : string <br>`time` : double <br>`value` : double <br> | `null`<br> |
| `Clip` | `createEventInPixelSpace` | `namePath` : string <br>`time` : double <br>`value` : double <br> | `null`<br> |
| `Clip` | `removeEvent` | `namePath` : string <br>`time` : double <br> | `null`<br> |
| `Clip` | `createPauseCueBeforeClip` | None | `handle`<br> |
| `Clip` | `setColorTransformPath` | `colorTransformPath` : string <br> | `null`<br> |
| `Clip` | `getColorTransformPath` | None | `string`<br> |
| `Clip` | `clearColorTransformPath` | None | `null`<br> |
| `Clip` | `getKeyframesAsJsonString` | None | `string`<br> |
#### Node
Syntax: *Pixera.Timelines.Node.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Node` | `getParameters` | None | `handle[]`<br> |
| `Node` | `getName` | None | `string`<br> |
| `Node` | `getParamWithName` | `name` : string <br> | `handle`<br> |
| `Node` | `setValues` | `values` : double[] <br> | `null`<br> |
| `Node` | `getValues` | None | `double[]`<br> |
| `Node` | `resetValues` | None | `null`<br> |
| `Node` | `storeValues` | None | `null`<br> |
| `Node` | `mute` | None | `null`<br> |
| `Node` | `unMute` | None | `null`<br> |
| `Node` | `getIsMuted` | None | `bool`<br> |
| `Node` | `getTimeline` | None | `handle`<br> |
| `Node` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Node` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Node` | `getInstancePath` | None | `string`<br> |
#### Param
Syntax: *Pixera.Timelines.Param.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Param` | `getName` | None | `string`<br> |
| `Param` | `getIsChannel` | None | `bool`<br> |
| `Param` | `setValue` | `value` : timelineParamValue <br> | `null`<br> |
| `Param` | `setValueRelativ` | `value` : double <br> | `null`<br> |
| `Param` | `getValue` | None | `timelineParamValue`<br> |
| `Param` | `resetValue` | None | `null`<br> |
| `Param` | `storeValue` | None | `null`<br> |
| `Param` | `setTransportAttributes` | `mode` : int <br>`speed` : double <br>`loop` : bool <br>`inpoint` : int <br>`outpoint` : int <br> | `null`<br> |
| `Param` | `getAttributes` | None | `TransportAttributes`<br> |
| `Param` | `mute` | None | `null`<br> |
| `Param` | `unMute` | None | `null`<br> |
| `Param` | `getIsMuted` | None | `bool`<br> |
| `Param` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Param` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Param` | `getInstancePath` | None | `string`<br> |
#### Cue
Syntax: *Pixera.Timelines.Cue.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Cue` | `removeThis` | None | `null`<br> |
| `Cue` | `apply` | None | `null`<br> |
| `Cue` | `blendToThis` | `blendDurationInSeconds` : double <br> | `null`<br> |
| `Cue` | `getAttributes` | None | `CueAttributes`<br> |
| `Cue` | `getTimeline` | None | `handle`<br> |
| `Cue` | `getIndex` | None | `int`<br> |
| `Cue` | `getName` | None | `string`<br> |
| `Cue` | `setName` | `name` : string <br> | `bool`<br> |
| `Cue` | `getNote` | None | `string`<br> |
| `Cue` | `setNote` | `note` : string <br> | `bool`<br> |
| `Cue` | `getOperation` | None | `int`<br> |
| `Cue` | `setOperation` | `operation` : int <br> | `bool`<br> |
| `Cue` | `getJumpMode` | None | `int`<br> |
| `Cue` | `setJumpMode` | `jumpMode` : int <br> | `bool`<br> |
| `Cue` | `getJumpGoalTime` | None | `double`<br> |
| `Cue` | `setJumpGoalTime` | `time` : double <br> | `bool`<br> |
| `Cue` | `getJumpGoalLabel` | None | `string`<br> |
| `Cue` | `getJumpGoalCue` | None | `handle`<br> |
| `Cue` | `setJumpGoalLabel` | `jumpGoalLabel` : string <br> | `bool`<br> |
| `Cue` | `getNumber` | None | `int`<br> |
| `Cue` | `setNumber` | `number` : int <br> | `null`<br> |
| `Cue` | `getWaitDuration` | None | `double`<br> |
| `Cue` | `setWaitDuration` | `time` : double <br> | `bool`<br> |
| `Cue` | `getBlendDuration` | None | `double`<br> |
| `Cue` | `setBlendDuration` | `timeInFrames` : double <br> | `bool`<br> |
| `Cue` | `getTime` | None | `double`<br> |
| `Cue` | `setTime` | `time` : double <br> | `bool`<br> |
| `Cue` | `getTimelineToTriggerName` | None | `string`<br> |
| `Cue` | `setTimelineToTrigger` | `nameTimeline` : string <br> | `bool`<br> |
| `Cue` | `getTimelineTriggerMode` | None | `int`<br> |
| `Cue` | `setTimelineTriggerMode` | `mode` : int <br> | `bool`<br> |
| `Cue` | `getTimelineTriggerApplyTime` | None | `double`<br> |
| `Cue` | `setTimelineTriggerApplyTime` | `time` : double <br> | `bool`<br> |
| `Cue` | `setTimelineTriggerApplyCue` | `goalCueLabel` : string <br> | `bool`<br> |
| `Cue` | `getCountdown` | None | `double`<br> |
| `Cue` | `getCountdownHMSF` | None | `string`<br> |
| `Cue` | `setCommand` | `conveyorName` : string <br>`commandData` : string <br> | `null`<br> |
| `Cue` | `getInst` | `instancePath` : string <br> | `handle`<br> |
| `Cue` | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle`<br> |
| `Cue` | `getInstancePath` | None | `string`<br> |

## Calibration
Syntax: *Pixera.Calibration.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `setMarkerPositions` | `positions` : double[] <br>`markerIds` : int[] <br> | `null`<br> |

## WebViews
Syntax: *Pixera.WebViews.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `loadDeviceUi` | `devicePath` : string <br> | `null`<br> |
| `activatePreviousFunc` | None | `null`<br> |
| `activateNextFunc` | None | `null`<br> |
| `getLastActivatedFunc` | None | `string`<br> |
| `deviceActivated` | `devicePath` : string <br>`withSelection` : bool <br> | `null`<br> |
| `funcActivated` | `funcPath` : string <br>`withSelection` : bool <br> | `null`<br> |
| `setFuncBodyState` | `funcPath` : string <br>`state` : string <br> | `null`<br> |
| `getFuncBodyState` | `funcPath` : string <br> | `string`<br> |
| `setTag` | `tag` : string <br>`text` : string <br> | `null`<br> |
| `setEditorIsUsingBlocks` | `useBlocks` : bool <br> | `null`<br> |

## Ui
Syntax: *Pixera.Ui.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getComboBoxWithId` | `id` : double <br> | `handle`<br> |
| `setAppMode` | `mode` : int <br> | `null`<br> |
| `getAppMode` | None | `int`<br> |
| `getDisplayTestpattern` | None | `bool`<br> |
| `setDisplayTestpattern` | `display` : bool <br> | `null`<br> |
| `getPreviewCameraAsJsonString` | None | `string`<br> |
| `setPreviewCameraAsJsonString` | `cameraFrustrumStateString` : string <br> | `null`<br> |
| `setDisableContentRendering` | `state` : bool <br> | `null`<br> |
| `getIsContentRenderingDisabled` | None | `bool`<br> |
| `setDisableWorkspaceRendering` | `state` : bool <br> | `null`<br> |
| `getIsWorkspaceRenderingDisabled` | None | `bool`<br> |
### Classes
#### ComboBox
Syntax: *Pixera.Ui.ComboBox.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `ComboBox` | `clear` | None | `null`<br> |
| `ComboBox` | `addItem` | `item` : string <br>`id` : int <br> | `null`<br> |
| `ComboBox` | `setSelectedId` | `id` : int <br> | `null`<br> |
| `ComboBox` | `getSelectedId` | None | `int`<br> |

## Direct
Syntax: *Pixera.Direct.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `setRegistered` | `hdls` : handle[] <br>`expectedFrequency` : int <br>`dampingMs` : int <br>`usageHints` : string[] <br> | `null`<br> |
| `reloadRegistered` | None | `null`<br> |
| `registerScreen` | `name` : string <br>`expectedFrequency` : int <br>`dampingMs` : int <br> | `handle`<br> |
| `registerParam` | `instancePath` : string <br> | `handle`<br> |
| `registerCamera` | `cameraName` : string <br>`expectedFrequency` : int <br> | `handle`<br> |
| `registerPerspective` | `screenName` : string <br>`expectedFrequency` : int <br> | `handle`<br> |
### Classes
#### Screen
Syntax: *Pixera.Direct.Screen.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Screen` | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null`<br> |
| `Screen` | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null`<br> |
| `Screen` | `setPosRot` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null`<br> |
| `Screen` | `setPosRotScale` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `null`<br> |
| `Screen` | `enableLogging` | `enable` : bool <br> | `null`<br> |
#### Param
Syntax: *Pixera.Direct.Param.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Param` | `setValue` | `value` : double <br> | `null`<br> |
| `Param` | `enableLogging` | `enable` : bool <br> | `null`<br> |
#### Camera
Syntax: *Pixera.Direct.Camera.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Camera` | `setPosition` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `null`<br> |
| `Camera` | `setRotation` | `xRot` : double <br>`yRot` : double <br>`zRot` : double <br> | `null`<br> |
| `Camera` | `setTransformation` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br> | `null`<br> |
| `Camera` | `setTransformationAndLensProps` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null`<br> |
| `Camera` | `setTransformationAndLensPropsExt` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`focalDistance` : double <br>`zoom` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`k3` : double <br>`p1` : double <br>`p2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br>`overscan` : double <br> | `null`<br> |
#### Perspective
Syntax: *Pixera.Direct.Perspective.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Perspective` | `setTransformation` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br> | `null`<br> |
| `Perspective` | `setTransformationAndLensProps` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null`<br> |

## Unreal
Syntax: *Pixera.Unreal.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getSupportedUnrealPluginVersion` | None | `int`<br> |

