
# Protocol Overview
This documentation describes revision 367 of the API.

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
| `Conveyor` | `sendString` | `handle` : object<br>`str` : string <br> | `null`<br> |

## Compound
Syntax: *Pixera.Compound.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `setTransportModeOnTimelineAtIndex` | `index` : int <br>`mode` : int <br> | `bool`<br> |
| `setTransportModeOnTimeline` | `timelineName` : string <br>`mode` : int <br> | `null`<br> |
| `toggleTransport` | `timelineName` : string <br> | `null`<br> |
| `getTransportModeOnTimeline` | `timelineName` : string <br> | `int`<br> |
| `startFirstTimeline` | None | `null`<br> |
| `pauseFirstTimeline` | None | `null`<br> |
| `stopFirstTimeline` | None | `null`<br> |
| `setOpacityOnTimeline` | `timelineName` : string <br>`opacity` : double <br> | `null`<br> |
| `getOpacityOnTimeline` | `timelineName` : string <br> | `double`<br> |
| `setPosValue` | `val` : double <br> | `null`<br> |
| `setPosValueXY` | `valX` : double <br>`valY` : double <br> | `null`<br> |
| `setParamValue` | `path` : string <br>`value` : double <br> | `null`<br> |
| `applyCueAtIndexOnTimelineAtIndex` | `cueIndex` : int <br>`timelineIndex` : int <br>`blendDuration` : optional<double> <br> | `null`<br> |
| `applyCueNumberOnTimelineAtIndex` | `cueNumber` : int <br>`timelineIndex` : int <br>`blendDuration` : optional<double> <br> | `null`<br> |
| `applyCueNumberOnTimeline` | `timelineName` : string <br>`cueNumber` : int <br>`blendDuration` : optional<double> <br> | `null`<br> |
| `applyCueOnTimeline` | `timelineName` : string <br>`cueName` : string <br>`blendDuration` : optional<double> <br> | `null`<br> |
| `addResourceToFolder` | `namePath` : string <br>`filePath` : string <br> | `handle`<br> |
| `assignResourceToLayer` | `resourcePath` : string <br>`layerPath` : string <br> | `null`<br> |
| `refreshResource` | `resourcePath` : string <br> | `null`<br> |
| `setTransportModeOnLayer` | `layerPath` : string <br>`mode` : int <br>`loop` : bool <br> | `null`<br> |
| `getTransportModeOnLayer` | `layerPath` : string <br> | `int`<br> |
| `getResourceAssignedToLayer` | `layerPath` : string <br> | `string`<br> |
| `assignResourceToClipAtTimeByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`time` : double <br> | `null`<br> |
| `assignResourceToClipAtHMSFStringByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`hmsf` : string <br> | `null`<br> |
| `assignResourceToClipAtHMSFByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`h` : int <br>`m` : int <br>`s` : int <br>`f` : int <br> | `null`<br> |
| `setCurrentTimeOfTimeline` | `name` : string <br>`time` : int <br> | `null`<br> |
| `setCurrentTimeOfTimelineInSeconds` | `name` : string <br>`time` : double <br> | `null`<br> |
| `setCurrentTimeAndTransportModeOfTimelineInSeconds` | `name` : string <br>`time` : double <br>`mode` : int <br> | `null`<br> |
| `getFpsOfTimeline` | `name` : string <br> | `double`<br> |
| `getCurrentTimeOfTimeline` | `name` : string <br> | `int`<br> |
| `getCurrentTimeOfTimelineInSeconds` | `name` : string <br> | `double`<br> |
| `getCurrentHMSFOfTimeline` | `name` : string <br> | `string`<br> |
| `getCurrentCountdownOfTimeline` | `name` : string <br> | `int`<br> |
| `getCurrentCountdownHMSFOfTimeline` | `name` : string <br> | `string`<br> |
| `blockUiTimelineUpdates` | `doBlock` : bool <br>`terminationDurationInMs` : optional<int> <br> | `null`<br> |
| `startOpacityAnimationOfTimeline` | `name` : string <br>`fadeIn` : bool <br>`fullFadeDuration` : double <br> | `null`<br> |
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
| `getUsagePresets` | None | `handle[]`<br> |
### Classes
#### MultiUserMember
Syntax: *Pixera.LiveSystems.MultiUserMember.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `MultiUserMember` | `getName` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `getIp` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `getState` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `getPerformanceMonitoringValuesJson` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `getPerformanceMonitoringValuesJsonEx` | `handle` : object<br>`filter` : string <br> | `string`<br> |
| `MultiUserMember` | `resetCumulativePerformanceMonitoringValues` | `handle` : object<br> | `null`<br> |
| `MultiUserMember` | `ensureFileDistribution` | `handle` : object<br>`includeNotUsedYet` : bool <br> | `null`<br> |
| `MultiUserMember` | `shutDown` | `handle` : object<br>`mode` : int <br> | `null`<br> |
| `MultiUserMember` | `wakeUp` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `getMacAddress` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `resetEngine` | `handle` : object<br> | `null`<br> |
| `MultiUserMember` | `restartEngine` | `handle` : object<br> | `null`<br> |
| `MultiUserMember` | `startEngine` | `handle` : object<br> | `null`<br> |
| `MultiUserMember` | `closeEngine` | `handle` : object<br> | `null`<br> |
| `MultiUserMember` | `triggerBackup` | `handle` : object<br>`applyControlCommand` : optional<bool> <br> | `null`<br> |
| `MultiUserMember` | `getStructureJson` | `handle` : object<br> | `string`<br> |
| `MultiUserMember` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
#### LiveSystem
Syntax: *Pixera.LiveSystems.LiveSystem.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `LiveSystem` | `ref` | `handle` : object<br> | `handle`<br> |
| `LiveSystem` | `getName` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `getIp` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `getState` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `setBackupRole` | `handle` : object<br>`role` : int <br> | `null`<br> |
| `LiveSystem` | `getBackupRole` | `handle` : object<br> | `int`<br> |
| `LiveSystem` | `getPerformanceMonitoringValuesJson` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `getPerformanceMonitoringValuesJsonEx` | `handle` : object<br>`filter` : string <br> | `string`<br> |
| `LiveSystem` | `resetCumulativePerformanceMonitoringValues` | `handle` : object<br> | `null`<br> |
| `LiveSystem` | `moveMappingsToOutputs` | `handle` : object<br>`hdlSrc` : handle <br>`outputIdPathMapStr` : string <br> | `null`<br> |
| `LiveSystem` | `setUsagePresetName` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `LiveSystem` | `getUsagePresetName` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `updateUsagePreset` | `handle` : object<br> | `null`<br> |
| `LiveSystem` | `saveUsagePresetAs` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `LiveSystem` | `applyUsagePreset` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `LiveSystem` | `exportUsagePreset` | `handle` : object<br>`path` : string <br> | `null`<br> |
| `LiveSystem` | `importUsagePreset` | `handle` : object<br>`path` : string <br> | `null`<br> |
| `LiveSystem` | `ensureFileDistribution` | `handle` : object<br>`includeNotUsedYet` : bool <br> | `null`<br> |
| `LiveSystem` | `shutDown` | `handle` : object<br>`mode` : int <br> | `null`<br> |
| `LiveSystem` | `wakeUp` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `getMacAddress` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `getGraphicsDevices` | `handle` : object<br> | `handle[]`<br> |
| `LiveSystem` | `getEnabledOutputs` | `handle` : object<br> | `handle[]`<br> |
| `LiveSystem` | `getAllOutputs` | `handle` : object<br> | `handle[]`<br> |
| `LiveSystem` | `getVideoStreamOutputs` | `handle` : object<br> | `handle[]`<br> |
| `LiveSystem` | `resetEngine` | `handle` : object<br> | `null`<br> |
| `LiveSystem` | `restartEngine` | `handle` : object<br> | `null`<br> |
| `LiveSystem` | `startEngine` | `handle` : object<br> | `null`<br> |
| `LiveSystem` | `closeEngine` | `handle` : object<br> | `null`<br> |
| `LiveSystem` | `setAudioMasterVolume` | `handle` : object<br>`channel` : int <br>`volume` : double <br> | `null`<br> |
| `LiveSystem` | `getAudioMasterVolume` | `handle` : object<br>`channel` : int <br> | `double`<br> |
| `LiveSystem` | `setAudioMasterMute` | `handle` : object<br>`channel` : int <br>`state` : bool <br> | `null`<br> |
| `LiveSystem` | `getAudioMasterMute` | `handle` : object<br>`channel` : int <br> | `bool`<br> |
| `LiveSystem` | `toggleAudioMasterMute` | `handle` : object<br>`channel` : int <br> | `null`<br> |
| `LiveSystem` | `setAudioTimecodeInput` | `handle` : object<br>`channel` : int <br>`state` : bool <br> | `null`<br> |
| `LiveSystem` | `triggerBackup` | `handle` : object<br>`applyControlCommand` : optional<bool> <br> | `null`<br> |
| `LiveSystem` | `getStructureJson` | `handle` : object<br> | `string`<br> |
| `LiveSystem` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `LiveSystem` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### UsagePreset
Syntax: *Pixera.LiveSystems.UsagePreset.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `UsagePreset` | `getName` | `handle` : object<br> | `string`<br> |
| `UsagePreset` | `update` | `handle` : object<br> | `null`<br> |
| `UsagePreset` | `apply` | `handle` : object<br>`destinationIp` : string <br> | `null`<br> |
| `UsagePreset` | `importFromFile` | `handle` : object<br>`path` : string <br> | `null`<br> |
| `UsagePreset` | `exportToFile` | `handle` : object<br>`path` : string <br> | `null`<br> |
| `UsagePreset` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `UsagePreset` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### GraphicsDevice
Syntax: *Pixera.LiveSystems.GraphicsDevice.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `GraphicsDevice` | `getName` | `handle` : object<br> | `string`<br> |
| `GraphicsDevice` | `getEnabledOutputs` | `handle` : object<br> | `handle[]`<br> |
| `GraphicsDevice` | `getAllOutputs` | `handle` : object<br> | `handle[]`<br> |
#### Output
Syntax: *Pixera.LiveSystems.Output.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Output` | `getName` | `handle` : object<br> | `string`<br> |
| `Output` | `setActive` | `handle` : object<br>`active` : bool <br> | `null`<br> |
| `Output` | `getActive` | `handle` : object<br> | `bool`<br> |
| `Output` | `setIdentify` | `handle` : object<br>`state` : bool <br> | `null`<br> |
| `Output` | `getIdentify` | `handle` : object<br> | `bool`<br> |
| `Output` | `getAssignedScreens` | `handle` : object<br> | `handle[]`<br> |
| `Output` | `getAssignedProjectors` | `handle` : object<br> | `handle[]`<br> |
| `Output` | `getEnabled` | `handle` : object<br> | `bool`<br> |
| `Output` | `getForPreview` | `handle` : object<br> | `bool`<br> |
| `Output` | `setIsOutputAggregate` | `handle` : object<br>`state` : bool <br> | `null`<br> |
| `Output` | `getIsOutputAggregate` | `handle` : object<br> | `bool`<br> |
| `Output` | `setAggregateDims` | `handle` : object<br>`horizontalCount` : int <br>`verticalCount` : int <br> | `null`<br> |
| `Output` | `getAggregateDims` | `handle` : object<br> | `int[]`<br> |
#### VideoStream
Syntax: *Pixera.LiveSystems.VideoStream.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `VideoStream` | `getName` | `handle` : object<br> | `string`<br> |
| `VideoStream` | `setActive` | `handle` : object<br>`active` : bool <br> | `null`<br> |
| `VideoStream` | `getActive` | `handle` : object<br> | `bool`<br> |

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
| `Screen` | `getId` | `handle` : object<br> | `double`<br> |
| `Screen` | `getName` | `handle` : object<br> | `string`<br> |
| `Screen` | `setPosition` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPosition` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setRotation` | `handle` : object<br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `getRotation` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setScale` | `handle` : object<br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `bool`<br> |
| `Screen` | `getScale` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setPosRot` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `setPosRotAndPerspectivePos` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`perspXPos` : optional<double> <br>`perspYPos` : optional<double> <br>`perspZPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `setPosRotScale` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPersepective` | `handle` : object<br> | `handle`<br> |
| `Screen` | `snapPerspectiveCornersToScreen` | `handle` : object<br>`mode` : int <br> | `null`<br> |
| `Screen` | `setPerspectivePosition` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `setPerspectivePositionWithLookAt` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPerspectivePosition` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setPerspectiveRotation` | `handle` : object<br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `getPerspectiveRotation` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setCameraPosition` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `setCameraPositionWithLookAt` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Screen` | `getCameraPosition` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setCameraRotation` | `handle` : object<br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Screen` | `getCameraRotation` | `handle` : object<br> | `ScreenPosValues`<br> |
| `Screen` | `setContentSamplingFrustumBase` | `handle` : object<br>`x` : double <br>`y` : double <br>`width` : double <br>`height` : double <br>`rotation` : double <br>`originScreenId` : double <br> | `null`<br> |
| `Screen` | `runCalibration` | `handle` : object<br>`mode` : string <br>`diff` : string <br> | `null`<br> |
| `Screen` | `editCalibration` | `handle` : object<br>`diff` : string <br> | `null`<br> |
| `Screen` | `resetWarpFile` | `handle` : object<br>`diff` : string <br> | `null`<br> |
| `Screen` | `loadWarpFile` | `handle` : object<br>`filePath` : string <br> | `null`<br> |
| `Screen` | `loadWarpFileWithDiff` | `handle` : object<br>`filePath` : string <br>`diff` : string <br> | `null`<br> |
| `Screen` | `addWarpFile` | `handle` : object<br>`filePath` : string <br> | `null`<br> |
| `Screen` | `addWarpFileWithDiff` | `handle` : object<br>`filePath` : string <br>`diff` : string <br> | `null`<br> |
| `Screen` | `loadColorCalibration` | `handle` : object<br>`calibrationName` : string <br> | `null`<br> |
| `Screen` | `runColorCalibration` | `handle` : object<br> | `null`<br> |
| `Screen` | `setIsVisible` | `handle` : object<br>`isVisible` : bool <br> | `null`<br> |
| `Screen` | `getIsVisible` | `handle` : object<br> | `bool`<br> |
| `Screen` | `setIsProjectable` | `handle` : object<br>`isProjectable` : bool <br> | `null`<br> |
| `Screen` | `getIsProjectable` | `handle` : object<br> | `bool`<br> |
| `Screen` | `triggerRefreshMapping` | `handle` : object<br> | `null`<br> |
| `Screen` | `resetAllColorCorrections` | `handle` : object<br> | `null`<br> |
| `Screen` | `setColorCorrectionWithPath` | `handle` : object<br>`path` : string <br>`value` : float <br> | `null`<br> |
| `Screen` | `getColorCorrectionWithPath` | `handle` : object<br>`path` : string <br> | `float`<br> |
| `Screen` | `setColorCorrectionAsJsonString` | `handle` : object<br>`colorCorrection` : string <br> | `null`<br> |
| `Screen` | `getColorCorrectionAsJsonString` | `handle` : object<br> | `string`<br> |
| `Screen` | `getOutput` | `handle` : object<br> | `handle[]`<br> |
| `Screen` | `setBlackout` | `handle` : object<br>`isActive` : bool <br> | `null`<br> |
| `Screen` | `getBlackout` | `handle` : object<br> | `bool`<br> |
| `Screen` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Screen` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Screen` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### StudioCamera
Syntax: *Pixera.Screens.StudioCamera.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `StudioCamera` | `getName` | `handle` : object<br> | `string`<br> |
| `StudioCamera` | `setPosition` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null`<br> |
| `StudioCamera` | `getPosition` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `double[]`<br> |
| `StudioCamera` | `setRotation` | `handle` : object<br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null`<br> |
| `StudioCamera` | `getRotation` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `double[]`<br> |
| `StudioCamera` | `setTransformation` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`fov` : optional<double> <br>`aspectRatio` : optional<double> <br> | `null`<br> |
| `StudioCamera` | `setTransformationAndLensProps` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null`<br> |
| `StudioCamera` | `setTransformationAndLensPropsExt` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`focalDistance` : double <br>`zoom` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`k3` : double <br>`p1` : double <br>`p2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br>`overscan` : double <br> | `null`<br> |
| `StudioCamera` | `setTrackingInputPause` | `handle` : object<br>`pause` : bool <br> | `null`<br> |
| `StudioCamera` | `getTrackingInputPause` | `handle` : object<br> | `bool`<br> |
| `StudioCamera` | `setUsePositionPropertiesFromTracking` | `handle` : object<br>`pause` : bool <br> | `null`<br> |
| `StudioCamera` | `getUsePositionPropertiesFromTracking` | `handle` : object<br> | `bool`<br> |
| `StudioCamera` | `setUseRotationPropertiesFromTracking` | `handle` : object<br>`pause` : bool <br> | `null`<br> |
| `StudioCamera` | `getUseRotationPropertiesFromTracking` | `handle` : object<br> | `bool`<br> |
| `StudioCamera` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `StudioCamera` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `StudioCamera` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### Perspective
Syntax: *Pixera.Screens.Perspective.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Perspective` | `getName` | `handle` : object<br> | `string`<br> |
| `Perspective` | `setTransformation` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`fov` : optional<double> <br>`aspectRatio` : optional<double> <br>`lockLookAtPt` : optional<bool> <br> | `null`<br> |
| `Perspective` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Perspective` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Perspective` | `getInstancePath` | `handle` : object<br> | `string`<br> |

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
| `Projector` | `getPosition` | `handle` : object<br> | `ProjectorPosValues`<br> |
| `Projector` | `setPosition` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool`<br> |
| `Projector` | `getRotation` | `handle` : object<br> | `ProjectorPosValues`<br> |
| `Projector` | `setRotation` | `handle` : object<br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool`<br> |
| `Projector` | `getName` | `handle` : object<br> | `string`<br> |
| `Projector` | `activateScreenMapping` | `handle` : object<br>`screenId` : double <br>`isActive` : bool <br> | `null`<br> |
| `Projector` | `setBlackout` | `handle` : object<br>`isActive` : bool <br> | `null`<br> |
| `Projector` | `getBlackout` | `handle` : object<br> | `bool`<br> |
| `Projector` | `setSoftedgeVisible` | `handle` : object<br>`screenName` : string <br>`visible` : bool <br> | `null`<br> |
| `Projector` | `resetAllColorCorrections` | `handle` : object<br> | `null`<br> |
| `Projector` | `setColorCorrectionWithPath` | `handle` : object<br>`path` : string <br>`value` : float <br> | `null`<br> |
| `Projector` | `getColorCorrectionWithPath` | `handle` : object<br>`path` : string <br> | `float`<br> |
| `Projector` | `setColorCorrectionAsJsonString` | `handle` : object<br>`colorCorrection` : string <br> | `null`<br> |
| `Projector` | `getColorCorrectionAsJsonString` | `handle` : object<br> | `string`<br> |
| `Projector` | `getOutput` | `handle` : object<br>`index` : optional<int> <br> | `handle`<br> |
| `Projector` | `setOutput` | `handle` : object<br>`outputHandle` : handle <br> | `null`<br> |
| `Projector` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Projector` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Projector` | `getInstancePath` | `handle` : object<br> | `string`<br> |

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
| `ResourceFolder` | `ref` | `handle` : object<br> | `handle`<br> |
| `ResourceFolder` | `getName` | `handle` : object<br> | `string`<br> |
| `ResourceFolder` | `setName` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `ResourceFolder` | `getResourceFolders` | `handle` : object<br> | `handle[]`<br> |
| `ResourceFolder` | `getResources` | `handle` : object<br> | `handle[]`<br> |
| `ResourceFolder` | `getResourceAtIndex` | `handle` : object<br>`index` : int <br> | `handle`<br> |
| `ResourceFolder` | `addResource` | `handle` : object<br>`path` : string <br> | `handle`<br> |
| `ResourceFolder` | `addResourcesFromDirectory` | `handle` : object<br>`path` : string <br>`removeOthers` : bool <br>`checkRedundancy` : bool <br> | `handle[]`<br> |
| `ResourceFolder` | `addResourcesFromDirectoryRemoveAssets` | `handle` : object<br>`path` : string <br>`removeOthers` : bool <br>`checkRedundancy` : bool <br> | `handle[]`<br> |
| `ResourceFolder` | `addInternalResource` | `handle` : object<br>`signature` : string <br>`resKind` : int <br> | `handle`<br> |
| `ResourceFolder` | `createFoldersFrom` | `handle` : object<br>`path` : string <br> | `null`<br> |
| `ResourceFolder` | `refreshResources` | `handle` : object<br> | `null`<br> |
| `ResourceFolder` | `moveResourceToThis` | `handle` : object<br>`id` : double <br> | `null`<br> |
| `ResourceFolder` | `removeThis` | `handle` : object<br> | `null`<br> |
| `ResourceFolder` | `removeThisIncludingAssets` | `handle` : object<br> | `null`<br> |
| `ResourceFolder` | `removeAllContents` | `handle` : object<br> | `null`<br> |
| `ResourceFolder` | `removeAllContentsIncludingAssets` | `handle` : object<br> | `null`<br> |
| `ResourceFolder` | `deleteAllContentsAssetsFromLiveSystem` | `handle` : object<br>`apEntityLiveSystemHandle` : handle <br> | `null`<br> |
| `ResourceFolder` | `resetDistributionTargets` | `handle` : object<br> | `null`<br> |
| `ResourceFolder` | `changeDistributionTarget` | `handle` : object<br>`apEntityLiveSystemHandle` : handle <br>`shouldDistribute` : bool <br> | `null`<br> |
| `ResourceFolder` | `replaceResourcesByString` | `handle` : object<br>`searchString` : string <br>`replaceString` : string <br>`path` : string <br> | `null`<br> |
| `ResourceFolder` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `ResourceFolder` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `ResourceFolder` | `getInstancePath` | `handle` : object<br> | `string`<br> |
| `ResourceFolder` | `getDmxId` | `handle` : object<br> | `int`<br> |
| `ResourceFolder` | `getCombinedDmxId` | `handle` : object<br> | `int`<br> |
| `ResourceFolder` | `setDmxId` | `handle` : object<br>`id` : int <br> | `null`<br> |
#### TranscodingFolder
Syntax: *Pixera.Resources.TranscodingFolder.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `TranscodingFolder` | `getUsedTranscodingPreset` | `handle` : object<br> | `string`<br> |
| `TranscodingFolder` | `setUsedTranscodingPreset` | `handle` : object<br>`preset` : string <br> | `null`<br> |
| `TranscodingFolder` | `getTranscodeAutomatically` | `handle` : object<br> | `bool`<br> |
| `TranscodingFolder` | `setTranscodeAutomatically` | `handle` : object<br>`autoTranscode` : bool <br> | `null`<br> |
| `TranscodingFolder` | `getUseRxCacheAsDestination` | `handle` : object<br> | `bool`<br> |
| `TranscodingFolder` | `setRxCacheAsDestination` | `handle` : object<br>`useRxCache` : bool <br> | `null`<br> |
| `TranscodingFolder` | `getDestinationDirectory` | `handle` : object<br> | `string`<br> |
| `TranscodingFolder` | `setDestinationDirectory` | `handle` : object<br>`path` : string <br> | `null`<br> |
#### Resource
Syntax: *Pixera.Resources.Resource.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Resource` | `ref` | `handle` : object<br> | `handle`<br> |
| `Resource` | `removeThis` | `handle` : object<br> | `null`<br> |
| `Resource` | `deleteFilesOnSystems` | `handle` : object<br> | `null`<br> |
| `Resource` | `removeThisIncludingAssets` | `handle` : object<br> | `null`<br> |
| `Resource` | `deleteAssetFromLiveSystem` | `handle` : object<br>`apEntityLiveSystemHandle` : handle <br> | `null`<br> |
| `Resource` | `resetDistributionTargets` | `handle` : object<br> | `null`<br> |
| `Resource` | `changeDistributionTarget` | `handle` : object<br>`apEntityLiveSystemHandle` : handle <br>`shouldDistribute` : bool <br> | `null`<br> |
| `Resource` | `getName` | `handle` : object<br> | `string`<br> |
| `Resource` | `setName` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `Resource` | `getFps` | `handle` : object<br> | `double`<br> |
| `Resource` | `getResolution` | `handle` : object<br> | `double[]`<br> |
| `Resource` | `getIsActive` | `handle` : object<br> | `bool`<br> |
| `Resource` | `getVideoStreamModes` | `handle` : object<br> | `string[]`<br> |
| `Resource` | `setVideoStreamMode` | `handle` : object<br>`index` : int <br> | `null`<br> |
| `Resource` | `getId` | `handle` : object<br> | `double`<br> |
| `Resource` | `getDuration` | `handle` : object<br> | `double`<br> |
| `Resource` | `getType` | `handle` : object<br> | `string`<br> |
| `Resource` | `setCurrentVersion` | `handle` : object<br>`version` : string <br> | `null`<br> |
| `Resource` | `getCurrentVersion` | `handle` : object<br> | `string`<br> |
| `Resource` | `getVersions` | `handle` : object<br> | `string[]`<br> |
| `Resource` | `getVersionSuffix` | `handle` : object<br> | `string[]`<br> |
| `Resource` | `rescanVersions` | `handle` : object<br> | `null`<br> |
| `Resource` | `getThumbnailAsBase64` | `handle` : object<br> | `string`<br> |
| `Resource` | `getHasPendingTransfer` | `handle` : object<br> | `bool`<br> |
| `Resource` | `getIsInUse` | `handle` : object<br> | `double`<br> |
| `Resource` | `getLastUsageBeginTime` | `handle` : object<br> | `double`<br> |
| `Resource` | `getLastUsageBeginTimeAsString` | `handle` : object<br> | `string`<br> |
| `Resource` | `getLastUsageEndTime` | `handle` : object<br> | `double`<br> |
| `Resource` | `getLastUsageEndTimeAsString` | `handle` : object<br> | `string`<br> |
| `Resource` | `getFilePath` | `handle` : object<br> | `string`<br> |
| `Resource` | `setText` | `handle` : object<br>`text` : string <br> | `null`<br> |
| `Resource` | `getText` | `handle` : object<br> | `string`<br> |
| `Resource` | `setFontWithName` | `handle` : object<br>`fontName` : string <br> | `bool`<br> |
| `Resource` | `getFontName` | `handle` : object<br> | `string`<br> |
| `Resource` | `setFontWithPath` | `handle` : object<br>`fontPath` : string <br> | `bool`<br> |
| `Resource` | `setHorizontalTextAlignment` | `handle` : object<br>`textAlignment` : int <br> | `bool`<br> |
| `Resource` | `getHorizontalTextAlignment` | `handle` : object<br> | `int`<br> |
| `Resource` | `setVerticalTextAlignment` | `handle` : object<br>`textAlignment` : int <br> | `bool`<br> |
| `Resource` | `getVerticalTextAlignment` | `handle` : object<br> | `int`<br> |
| `Resource` | `setLineHeight` | `handle` : object<br>`lineHeight` : double <br> | `bool`<br> |
| `Resource` | `getLineHeight` | `handle` : object<br> | `double`<br> |
| `Resource` | `getTextMeasurementsWidthAndHeight` | `handle` : object<br> | `int[]`<br> |
| `Resource` | `setUrl` | `handle` : object<br>`url` : string <br> | `null`<br> |
| `Resource` | `getUrl` | `handle` : object<br> | `string`<br> |
| `Resource` | `setColorTransformPath` | `handle` : object<br>`colorTransformPath` : string <br> | `null`<br> |
| `Resource` | `getColorTransformPath` | `handle` : object<br> | `string`<br> |
| `Resource` | `clearColorTransformPath` | `handle` : object<br> | `null`<br> |
| `Resource` | `refresh` | `handle` : object<br>`text` : string <br> | `null`<br> |
| `Resource` | `distribute` | `handle` : object<br> | `null`<br> |
| `Resource` | `getDmxId` | `handle` : object<br> | `int`<br> |
| `Resource` | `setDmxId` | `handle` : object<br>`id` : int <br> | `null`<br> |
| `Resource` | `removeMultiresourceIndex` | `handle` : object<br>`index` : int <br> | `null`<br> |
| `Resource` | `addMultiresourceItem` | `handle` : object<br>`id` : double <br> | `null`<br> |
| `Resource` | `getMultiresourceItems` | `handle` : object<br> | `handle[]`<br> |
| `Resource` | `replaceMultiresourceItemByIndex` | `handle` : object<br>`index` : int <br>`id` : double <br> | `null`<br> |
| `Resource` | `setMultiresourceResolution` | `handle` : object<br>`width` : int <br>`height` : int <br> | `null`<br> |
| `Resource` | `setMultiresourceItemSizebyIndex` | `handle` : object<br>`index` : int <br>`width` : double <br>`height` : double <br> | `null`<br> |
| `Resource` | `setMultiresourceItemPositionbyIndex` | `handle` : object<br>`index` : int <br>`x` : double <br>`y` : double <br> | `null`<br> |
| `Resource` | `setUseGradient` | `handle` : object<br>`useGradient` : bool <br> | `null`<br> |
| `Resource` | `getUseGradient` | `handle` : object<br> | `bool`<br> |
| `Resource` | `setColors` | `handle` : object<br>`argbCols` : uint[] <br>`positions` : double[] <br>`colNames` : string[] <br>`useGradient` : optional<bool> <br> | `null`<br> |
| `Resource` | `setColorAtIndex` | `handle` : object<br>`index` : int <br>`red` : int <br>`green` : int <br>`blue` : int <br>`alpha` : int <br>`position` : double <br>`name` : string <br>`useGradient` : optional<bool> <br> | `null`<br> |
| `Resource` | `getColorAtIndex` | `handle` : object<br>`colorIndex` : int <br> | `int`<br> |
| `Resource` | `getColorPositionAtIndex` | `handle` : object<br>`colorIndex` : int <br> | `double`<br> |
| `Resource` | `launchVirtualWorld` | `handle` : object<br>`action` : string <br> | `null`<br> |
| `Resource` | `getUnrealWorld` | `handle` : object<br> | `handle`<br> |
| `Resource` | `setMultiResourceItemRestrictedServiceIps` | `handle` : object<br>`itemIndex` : int <br>`ipAdresses` : string[] <br> | `null`<br> |
| `Resource` | `getMultiResourceItemRestrictedServiceIps` | `handle` : object<br>`itemIndex` : int <br> | `string[]`<br> |
| `Resource` | `replace` | `handle` : object<br>`path` : string <br> | `null`<br> |
| `Resource` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Resource` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Resource` | `getInstancePath` | `handle` : object<br> | `string`<br> |
| `Resource` | `transcodeWithExisitngPreset` | `handle` : object<br>`presetName` : string <br>`useRxCache` : bool <br>`destinationPath` : string <br>`startFrame` : int <br>`endFrame` : int <br>`serviceId` : uint <br> | `null`<br> |
| `Resource` | `transcodeWithSettings` | `handle` : object<br>`settings` : string <br>`useRxCache` : bool <br>`destinationPath` : string <br>`startFrame` : int <br>`endFrame` : int <br>`serviceId` : uint <br> | `null`<br> |
| `Resource` | `moveToTranscodingFolder` | `handle` : object<br>`folderPath` : string <br> | `null`<br> |
#### UnrealWorld
Syntax: *Pixera.Resources.UnrealWorld.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `UnrealWorld` | `getLevelNames` | `handle` : object<br> | `string[]`<br> |
| `UnrealWorld` | `loadLevel` | `handle` : object<br>`levelName` : string <br> | `null`<br> |
| `UnrealWorld` | `getEventTriggerNames` | `handle` : object<br> | `string[]`<br> |
| `UnrealWorld` | `triggerEventByName` | `handle` : object<br>`triggerName` : string <br> | `null`<br> |
| `UnrealWorld` | `createNDisplayConfig` | `handle` : object<br> | `null`<br> |
| `UnrealWorld` | `runUnreal` | `handle` : object<br> | `null`<br> |
| `UnrealWorld` | `killUnreal` | `handle` : object<br> | `null`<br> |
| `UnrealWorld` | `getName` | `handle` : object<br> | `string`<br> |
| `UnrealWorld` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `UnrealWorld` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `UnrealWorld` | `getInstancePath` | `handle` : object<br> | `string`<br> |

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
| `Timeline` | `ref` | `handle` : object<br> | `handle`<br> |
| `Timeline` | `removeThis` | `handle` : object<br> | `null`<br> |
| `Timeline` | `duplicateThis` | `handle` : object<br>`withoutClipsCues` : optional<bool> <br> | `handle`<br> |
| `Timeline` | `selectThis` | `handle` : object<br> | `null`<br> |
| `Timeline` | `getZoomFactor` | `handle` : object<br> | `double`<br> |
| `Timeline` | `setZoomFactor` | `handle` : object<br>`zoomFactor` : double <br> | `null`<br> |
| `Timeline` | `getVerticalScrollOffset` | `handle` : object<br> | `int`<br> |
| `Timeline` | `setVerticalScrollOffset` | `handle` : object<br>`offset` : int <br> | `null`<br> |
| `Timeline` | `getHorizontalScrollOffset` | `handle` : object<br> | `int`<br> |
| `Timeline` | `setHorizontalScrollOffset` | `handle` : object<br>`offset` : int <br> | `null`<br> |
| `Timeline` | `moveInRenderOrder` | `handle` : object<br>`moveDown` : bool <br> | `null`<br> |
| `Timeline` | `getLayers` | `handle` : object<br> | `handle[]`<br> |
| `Timeline` | `getLayerNames` | `handle` : object<br> | `string[]`<br> |
| `Timeline` | `getLayersSelected` | `handle` : object<br> | `handle[]`<br> |
| `Timeline` | `selectLayerByIndex` | `handle` : object<br>`index` : int <br> | `null`<br> |
| `Timeline` | `selectLayerByNames` | `handle` : object<br>`layerNames` : string[] <br> | `null`<br> |
| `Timeline` | `getLayerAtIndex` | `handle` : object<br>`index` : int <br> | `handle`<br> |
| `Timeline` | `createLayer` | `handle` : object<br> | `handle`<br> |
| `Timeline` | `getCueInfosAsJsonString` | `handle` : object<br> | `string`<br> |
| `Timeline` | `getCues` | `handle` : object<br> | `handle[]`<br> |
| `Timeline` | `getCueNames` | `handle` : object<br> | `string[]`<br> |
| `Timeline` | `getCueAtIndex` | `handle` : object<br>`index` : int <br> | `handle`<br> |
| `Timeline` | `getCueFromName` | `handle` : object<br>`name` : string <br> | `handle`<br> |
| `Timeline` | `getCueFromNumber` | `handle` : object<br>`number` : int <br> | `handle`<br> |
| `Timeline` | `applyCueWithName` | `handle` : object<br>`name` : string <br>`blendDuration` : optional<double> <br> | `null`<br> |
| `Timeline` | `applyCueWithNumber` | `handle` : object<br>`number` : int <br>`blendDuration` : optional<double> <br> | `null`<br> |
| `Timeline` | `createCue` | `handle` : object<br>`name` : string <br>`timeInFrames` : double <br>`operation` : int <br> | `handle`<br> |
| `Timeline` | `removeCues` | `handle` : object<br> | `null`<br> |
| `Timeline` | `createPauseCueBeforeSelectedClips` | `handle` : object<br> | `null`<br> |
| `Timeline` | `play` | `handle` : object<br> | `null`<br> |
| `Timeline` | `pause` | `handle` : object<br> | `null`<br> |
| `Timeline` | `stop` | `handle` : object<br> | `null`<br> |
| `Timeline` | `toggleTransport` | `handle` : object<br> | `null`<br> |
| `Timeline` | `store` | `handle` : object<br> | `null`<br> |
| `Timeline` | `reset` | `handle` : object<br> | `null`<br> |
| `Timeline` | `getAttributes` | `handle` : object<br> | `TimelineAttributes`<br> |
| `Timeline` | `setCurrentFrame` | `handle` : object<br>`time` : int <br> | `bool`<br> |
| `Timeline` | `setCurrentTime` | `handle` : object<br>`time` : int <br> | `null`<br> |
| `Timeline` | `getCurrentTime` | `handle` : object<br> | `int`<br> |
| `Timeline` | `scrubCurrentTime` | `handle` : object<br>`frames` : int <br> | `null`<br> |
| `Timeline` | `CurrentTime` | `handle` : object<br>`time` : int <br>`doSet` : bool <br> | `int`<br> |
| `Timeline` | `getCurrentHMSF` | `handle` : object<br> | `string`<br> |
| `Timeline` | `setTransportMode` | `handle` : object<br>`mode` : int <br> | `bool`<br> |
| `Timeline` | `getTransportMode` | `handle` : object<br> | `int`<br> |
| `Timeline` | `setTimecodeInput` | `handle` : object<br>`hour` : int <br>`minute` : int <br>`second` : int <br>`frame` : int <br>`elapsedTime` : double <br>`running` : bool <br>`freshMode` : int <br>`stateToken` : int <br>`format` : int <br> | `double`<br> |
| `Timeline` | `getFps` | `handle` : object<br> | `double`<br> |
| `Timeline` | `getName` | `handle` : object<br> | `string`<br> |
| `Timeline` | `setName` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `Timeline` | `moveToNextCue` | `handle` : object<br> | `null`<br> |
| `Timeline` | `moveToNextCueIgnoreProperties` | `handle` : object<br> | `null`<br> |
| `Timeline` | `getCueNext` | `handle` : object<br> | `handle`<br> |
| `Timeline` | `moveToPreviousCue` | `handle` : object<br> | `null`<br> |
| `Timeline` | `moveToPreviousCueIgnoreProperties` | `handle` : object<br> | `null`<br> |
| `Timeline` | `getCuePrevious` | `handle` : object<br> | `handle`<br> |
| `Timeline` | `ignoreNextCue` | `handle` : object<br> | `null`<br> |
| `Timeline` | `ignoreNextCueWithOperation` | `handle` : object<br>`cueOperation` : int <br> | `null`<br> |
| `Timeline` | `blendToTime` | `handle` : object<br>`goalTime` : double <br>`blendDuration` : double <br>`preloadDelayInMilliseconds` : optional<int> <br> | `null`<br> |
| `Timeline` | `blendToTimeWithTransportMode` | `handle` : object<br>`goalTime` : double <br>`blendDuration` : double <br>`transportMode` : int <br>`preloadDelayInMilliseconds` : optional<int> <br> | `null`<br> |
| `Timeline` | `setBlendToTimeMode` | `handle` : object<br>`mode` : int <br> | `bool`<br> |
| `Timeline` | `setSpeedFactor` | `handle` : object<br>`factor` : double <br> | `null`<br> |
| `Timeline` | `getSpeedFactor` | `handle` : object<br> | `double`<br> |
| `Timeline` | `setOpacity` | `handle` : object<br>`value` : double <br> | `null`<br> |
| `Timeline` | `getOpacity` | `handle` : object<br> | `double`<br> |
| `Timeline` | `startOpacityAnimation` | `handle` : object<br>`fadeIn` : bool <br>`fullFadeDuration` : double <br> | `null`<br> |
| `Timeline` | `setSmpteMode` | `handle` : object<br>`mode` : int <br> | `null`<br> |
| `Timeline` | `getSmpteMode` | `handle` : object<br> | `int`<br> |
| `Timeline` | `storeRecordedValues` | `handle` : object<br> | `null`<br> |
| `Timeline` | `setSmpteInputBehaviour` | `handle` : object<br>`mode` : int <br> | `null`<br> |
| `Timeline` | `getSmpteInputBehaviour` | `handle` : object<br> | `int`<br> |
| `Timeline` | `setSmpteOffset` | `handle` : object<br>`time` : double <br> | `null`<br> |
| `Timeline` | `getSmpteOffset` | `handle` : object<br> | `double`<br> |
| `Timeline` | `resetRecordedValues` | `handle` : object<br> | `null`<br> |
| `Timeline` | `getTimelineInfosAsJsonString` | `handle` : object<br> | `string`<br> |
| `Timeline` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Timeline` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Timeline` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### Layer
Syntax: *Pixera.Timelines.Layer.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Layer` | `ref` | `handle` : object<br> | `handle`<br> |
| `Layer` | `removeThis` | `handle` : object<br> | `null`<br> |
| `Layer` | `getNodes` | `handle` : object<br> | `handle[]`<br> |
| `Layer` | `getNodeWithName` | `handle` : object<br>`name` : string <br> | `handle`<br> |
| `Layer` | `getParamWithName` | `handle` : object<br>`name` : string <br> | `handle`<br> |
| `Layer` | `getSpatialParametersAtTime` | `handle` : object<br>`time` : double <br> | `double[]`<br> |
| `Layer` | `getTimeline` | `handle` : object<br> | `handle`<br> |
| `Layer` | `setName` | `handle` : object<br>`name` : string <br> | `null`<br> |
| `Layer` | `getName` | `handle` : object<br> | `string`<br> |
| `Layer` | `resetLayer` | `handle` : object<br> | `null`<br> |
| `Layer` | `getLayerJsonDescrip` | `handle` : object<br> | `string`<br> |
| `Layer` | `setLayerJsonDescrip` | `handle` : object<br>`descrip` : string <br>`makeAllDominant` : bool <br> | `null`<br> |
| `Layer` | `getJsonDescrip` | `handle` : object<br> | `string`<br> |
| `Layer` | `initFromJsonDescrip` | `handle` : object<br>`descrip` : string <br> | `null`<br> |
| `Layer` | `setOpacity` | `handle` : object<br>`value` : double <br> | `null`<br> |
| `Layer` | `getOpacity` | `handle` : object<br> | `double`<br> |
| `Layer` | `resetOpacity` | `handle` : object<br> | `null`<br> |
| `Layer` | `setVolume` | `handle` : object<br>`value` : double <br> | `null`<br> |
| `Layer` | `getVolume` | `handle` : object<br> | `double`<br> |
| `Layer` | `resetVolume` | `handle` : object<br> | `null`<br> |
| `Layer` | `muteLayer` | `handle` : object<br> | `null`<br> |
| `Layer` | `unMuteLayer` | `handle` : object<br> | `null`<br> |
| `Layer` | `getIsLayerMuted` | `handle` : object<br> | `bool`<br> |
| `Layer` | `muteAudio` | `handle` : object<br> | `null`<br> |
| `Layer` | `unMuteAudio` | `handle` : object<br> | `null`<br> |
| `Layer` | `getIsAudioMuted` | `handle` : object<br> | `bool`<br> |
| `Layer` | `getDmxMuteState` | `handle` : object<br> | `int`<br> |
| `Layer` | `setDmxMuteState` | `handle` : object<br>`muteState` : uint <br> | `null`<br> |
| `Layer` | `toggleExplicitMute` | `handle` : object<br>`flag` : uint <br> | `null`<br> |
| `Layer` | `setTransport` | `handle` : object<br>`mode` : int <br>`loop` : bool <br> | `null`<br> |
| `Layer` | `getTransportMode` | `handle` : object<br> | `int`<br> |
| `Layer` | `resetTransportMode` | `handle` : object<br> | `null`<br> |
| `Layer` | `getTransportLoop` | `handle` : object<br> | `bool`<br> |
| `Layer` | `assignResource` | `handle` : object<br>`id` : double <br> | `null`<br> |
| `Layer` | `assignResourceWithFade` | `handle` : object<br>`id` : double <br>`fadeDuration` : double <br> | `null`<br> |
| `Layer` | `getAssignedResource` | `handle` : object<br> | `handle`<br> |
| `Layer` | `resetAssignedResource` | `handle` : object<br> | `null`<br> |
| `Layer` | `getAssignedModelResource` | `handle` : object<br> | `handle`<br> |
| `Layer` | `resetAssignedModelResource` | `handle` : object<br> | `null`<br> |
| `Layer` | `getFxNames` | `handle` : object<br> | `string[]`<br> |
| `Layer` | `setFadeDurationDominantResourceChange` | `handle` : object<br>`value` : double <br> | `null`<br> |
| `Layer` | `getFadeDurationDominantResourceChange` | `handle` : object<br> | `double`<br> |
| `Layer` | `createClip` | `handle` : object<br> | `handle`<br> |
| `Layer` | `createClipAtTime` | `handle` : object<br>`timeInFrames` : double <br> | `handle`<br> |
| `Layer` | `controlClipBorder` | `handle` : object<br>`clip` : handle <br>`isEnter` : bool <br>`isIncremental` : bool <br>`entryTime` : double <br> | `null`<br> |
| `Layer` | `getClipAtIndex` | `handle` : object<br>`index` : int <br> | `handle`<br> |
| `Layer` | `getClips` | `handle` : object<br> | `handle[]`<br> |
| `Layer` | `getClipCurrent` | `handle` : object<br>`offset` : int <br> | `handle`<br> |
| `Layer` | `getClipsSelected` | `handle` : object<br> | `handle[]`<br> |
| `Layer` | `removeClips` | `handle` : object<br> | `null`<br> |
| `Layer` | `setHomeScreenFromScreenName` | `handle` : object<br>`screenName` : string <br> | `null`<br> |
| `Layer` | `getHomeScreenName` | `handle` : object<br> | `string`<br> |
| `Layer` | `setBlendMode` | `handle` : object<br>`blendMode` : string <br> | `null`<br> |
| `Layer` | `getBlendMode` | `handle` : object<br> | `string`<br> |
| `Layer` | `addEffectById` | `handle` : object<br>`id` : double <br> | `null`<br> |
| `Layer` | `setPreloadPermanently` | `handle` : object<br>`doPreloadPermanently` : bool <br> | `null`<br> |
| `Layer` | `getPreloadPermanently` | `handle` : object<br> | `bool`<br> |
| `Layer` | `setRestrictToServiceWithIps` | `handle` : object<br>`doRestrict` : bool <br>`ipAdresses` : string[] <br> | `null`<br> |
| `Layer` | `getRestrictToService` | `handle` : object<br> | `bool`<br> |
| `Layer` | `getRestrictedServiceIps` | `handle` : object<br> | `string[]`<br> |
| `Layer` | `getOffsets` | `handle` : object<br> | `double[]`<br> |
| `Layer` | `setOffsets` | `handle` : object<br>`x` : optional<double> <br>`y` : optional<double> <br>`z` : optional<double> <br>`xr` : optional<double> <br>`yr` : optional<double> <br>`zr` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `null`<br> |
| `Layer` | `setCurrentValuesToOffset` | `handle` : object<br>`typeIndex` : int <br>`resetDominant` : optional<bool> <br>`removeKeyframesClips` : optional<bool> <br> | `null`<br> |
| `Layer` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Layer` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Layer` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### Clip
Syntax: *Pixera.Timelines.Clip.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Clip` | `getId` | `handle` : object<br> | `double`<br> |
| `Clip` | `removeThis` | `handle` : object<br> | `null`<br> |
| `Clip` | `getTimeline` | `handle` : object<br> | `handle`<br> |
| `Clip` | `setTime` | `handle` : object<br>`time` : double <br> | `null`<br> |
| `Clip` | `getTime` | `handle` : object<br> | `double`<br> |
| `Clip` | `setDuration` | `handle` : object<br>`duration` : double <br> | `null`<br> |
| `Clip` | `getDuration` | `handle` : object<br> | `double`<br> |
| `Clip` | `setLabel` | `handle` : object<br>`label` : string <br> | `null`<br> |
| `Clip` | `getLabel` | `handle` : object<br> | `string`<br> |
| `Clip` | `getPlayMode` | `handle` : object<br> | `int`<br> |
| `Clip` | `setPlayMode` | `handle` : object<br>`playMode` : int <br> | `null`<br> |
| `Clip` | `getSpeed` | `handle` : object<br> | `double`<br> |
| `Clip` | `setSpeed` | `handle` : object<br>`speed` : double <br> | `null`<br> |
| `Clip` | `getBlendFrames` | `handle` : object<br> | `bool`<br> |
| `Clip` | `setBlendFrames` | `handle` : object<br>`doFrameblending` : bool <br> | `null`<br> |
| `Clip` | `getInpoint` | `handle` : object<br> | `double`<br> |
| `Clip` | `setInpoint` | `handle` : object<br>`inpoint` : double <br> | `null`<br> |
| `Clip` | `getOutpoint` | `handle` : object<br> | `double`<br> |
| `Clip` | `setOutpoint` | `handle` : object<br>`inpoint` : double <br> | `null`<br> |
| `Clip` | `assignResource` | `handle` : object<br>`resId` : double <br>`setToResourceDuration` : optional<bool> <br> | `null`<br> |
| `Clip` | `getAssignedResource` | `handle` : object<br> | `handle`<br> |
| `Clip` | `setToResourceDuration` | `handle` : object<br> | `null`<br> |
| `Clip` | `createEvent` | `handle` : object<br>`namePath` : string <br>`time` : double <br>`value` : double <br> | `null`<br> |
| `Clip` | `createEventInPixelSpace` | `handle` : object<br>`namePath` : string <br>`time` : double <br>`value` : double <br> | `null`<br> |
| `Clip` | `removeEvent` | `handle` : object<br>`namePath` : string <br>`time` : double <br> | `null`<br> |
| `Clip` | `createPauseCueBeforeClip` | `handle` : object<br> | `handle`<br> |
| `Clip` | `setColorTransformPath` | `handle` : object<br>`colorTransformPath` : string <br> | `null`<br> |
| `Clip` | `getColorTransformPath` | `handle` : object<br> | `string`<br> |
| `Clip` | `clearColorTransformPath` | `handle` : object<br> | `null`<br> |
| `Clip` | `getKeyframesAsJsonString` | `handle` : object<br> | `string`<br> |
#### Node
Syntax: *Pixera.Timelines.Node.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Node` | `getParameters` | `handle` : object<br> | `handle[]`<br> |
| `Node` | `getName` | `handle` : object<br> | `string`<br> |
| `Node` | `getParamWithName` | `handle` : object<br>`name` : string <br> | `handle`<br> |
| `Node` | `setValues` | `handle` : object<br>`values` : double[] <br> | `null`<br> |
| `Node` | `getValues` | `handle` : object<br> | `double[]`<br> |
| `Node` | `resetValues` | `handle` : object<br> | `null`<br> |
| `Node` | `storeValues` | `handle` : object<br> | `null`<br> |
| `Node` | `mute` | `handle` : object<br> | `null`<br> |
| `Node` | `unMute` | `handle` : object<br> | `null`<br> |
| `Node` | `toggleMute` | `handle` : object<br> | `null`<br> |
| `Node` | `getIsMuted` | `handle` : object<br> | `bool`<br> |
| `Node` | `getTimeline` | `handle` : object<br> | `handle`<br> |
| `Node` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Node` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Node` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### Param
Syntax: *Pixera.Timelines.Param.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Param` | `getName` | `handle` : object<br> | `string`<br> |
| `Param` | `getIsChannel` | `handle` : object<br> | `bool`<br> |
| `Param` | `setValue` | `handle` : object<br>`value` : timelineParamValue <br> | `null`<br> |
| `Param` | `setValueRelativ` | `handle` : object<br>`value` : double <br> | `null`<br> |
| `Param` | `getValue` | `handle` : object<br> | `timelineParamValue`<br> |
| `Param` | `resetValue` | `handle` : object<br> | `null`<br> |
| `Param` | `storeValue` | `handle` : object<br> | `null`<br> |
| `Param` | `setTransportAttributes` | `handle` : object<br>`mode` : int <br>`speed` : double <br>`loop` : bool <br>`inpoint` : int <br>`outpoint` : int <br> | `null`<br> |
| `Param` | `getAttributes` | `handle` : object<br> | `TransportAttributes`<br> |
| `Param` | `mute` | `handle` : object<br> | `null`<br> |
| `Param` | `unMute` | `handle` : object<br> | `null`<br> |
| `Param` | `toggleMute` | `handle` : object<br> | `null`<br> |
| `Param` | `getIsMuted` | `handle` : object<br> | `bool`<br> |
| `Param` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Param` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Param` | `getInstancePath` | `handle` : object<br> | `string`<br> |
#### Cue
Syntax: *Pixera.Timelines.Cue.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Cue` | `removeThis` | `handle` : object<br> | `null`<br> |
| `Cue` | `apply` | `handle` : object<br>`blendDuration` : optional<double> <br> | `null`<br> |
| `Cue` | `blendToThis` | `handle` : object<br>`blendDuration` : double <br> | `null`<br> |
| `Cue` | `getAttributes` | `handle` : object<br> | `CueAttributes`<br> |
| `Cue` | `getTimeline` | `handle` : object<br> | `handle`<br> |
| `Cue` | `getIndex` | `handle` : object<br> | `int`<br> |
| `Cue` | `getName` | `handle` : object<br> | `string`<br> |
| `Cue` | `setName` | `handle` : object<br>`name` : string <br> | `bool`<br> |
| `Cue` | `getNote` | `handle` : object<br> | `string`<br> |
| `Cue` | `setNote` | `handle` : object<br>`note` : string <br> | `bool`<br> |
| `Cue` | `getOperation` | `handle` : object<br> | `int`<br> |
| `Cue` | `setOperation` | `handle` : object<br>`operation` : int <br> | `bool`<br> |
| `Cue` | `getJumpMode` | `handle` : object<br> | `int`<br> |
| `Cue` | `setJumpMode` | `handle` : object<br>`jumpMode` : int <br> | `bool`<br> |
| `Cue` | `getJumpGoalTime` | `handle` : object<br> | `double`<br> |
| `Cue` | `setJumpGoalTime` | `handle` : object<br>`time` : double <br> | `bool`<br> |
| `Cue` | `getJumpGoalLabel` | `handle` : object<br> | `string`<br> |
| `Cue` | `getJumpGoalCue` | `handle` : object<br> | `handle`<br> |
| `Cue` | `setJumpGoalLabel` | `handle` : object<br>`jumpGoalLabel` : string <br> | `bool`<br> |
| `Cue` | `getNumber` | `handle` : object<br> | `int`<br> |
| `Cue` | `setNumber` | `handle` : object<br>`number` : int <br> | `null`<br> |
| `Cue` | `getWaitDuration` | `handle` : object<br> | `double`<br> |
| `Cue` | `setWaitDuration` | `handle` : object<br>`time` : double <br> | `bool`<br> |
| `Cue` | `getBlendDuration` | `handle` : object<br> | `double`<br> |
| `Cue` | `setBlendDuration` | `handle` : object<br>`timeInFrames` : double <br> | `bool`<br> |
| `Cue` | `getTime` | `handle` : object<br> | `double`<br> |
| `Cue` | `setTime` | `handle` : object<br>`time` : double <br> | `bool`<br> |
| `Cue` | `getTimelineToTriggerName` | `handle` : object<br> | `string`<br> |
| `Cue` | `setTimelineToTrigger` | `handle` : object<br>`nameTimeline` : string <br> | `bool`<br> |
| `Cue` | `getTimelineTriggerMode` | `handle` : object<br> | `int`<br> |
| `Cue` | `setTimelineTriggerMode` | `handle` : object<br>`mode` : int <br> | `bool`<br> |
| `Cue` | `getTimelineTriggerApplyTime` | `handle` : object<br> | `double`<br> |
| `Cue` | `setTimelineTriggerApplyTime` | `handle` : object<br>`time` : double <br> | `bool`<br> |
| `Cue` | `setTimelineTriggerApplyCue` | `handle` : object<br>`goalCueLabel` : string <br> | `bool`<br> |
| `Cue` | `isActive` | `handle` : object<br> | `bool`<br> |
| `Cue` | `setActivity` | `handle` : object<br>`idState` : int <br> | `null`<br> |
| `Cue` | `getCountdown` | `handle` : object<br> | `double`<br> |
| `Cue` | `getCountdownHMSF` | `handle` : object<br> | `string`<br> |
| `Cue` | `setCommand` | `handle` : object<br>`conveyorName` : string <br>`commandData` : string <br> | `null`<br> |
| `Cue` | `getInst` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Cue` | `getHandleFromInstancePath` | `handle` : object<br>`instancePath` : string <br> | `handle`<br> |
| `Cue` | `getInstancePath` | `handle` : object<br> | `string`<br> |

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
| `ComboBox` | `clear` | `handle` : object<br> | `null`<br> |
| `ComboBox` | `addItem` | `handle` : object<br>`item` : string <br>`id` : int <br> | `null`<br> |
| `ComboBox` | `setSelectedId` | `handle` : object<br>`id` : int <br> | `null`<br> |
| `ComboBox` | `getSelectedId` | `handle` : object<br> | `int`<br> |

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
| `Screen` | `setPosition` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null`<br> |
| `Screen` | `setRotation` | `handle` : object<br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null`<br> |
| `Screen` | `setPosRot` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null`<br> |
| `Screen` | `setPosRotAndPerspectivePos` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`perspXPos` : optional<double> <br>`perspYPos` : optional<double> <br>`perspZPos` : optional<double> <br> | `null`<br> |
| `Screen` | `setPosRotScale` | `handle` : object<br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `null`<br> |
| `Screen` | `enableLogging` | `handle` : object<br>`enable` : bool <br> | `null`<br> |
#### Param
Syntax: *Pixera.Direct.Param.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Param` | `setValue` | `handle` : object<br>`value` : double <br> | `null`<br> |
| `Param` | `enableLogging` | `handle` : object<br>`enable` : bool <br> | `null`<br> |
#### Camera
Syntax: *Pixera.Direct.Camera.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Camera` | `setPosition` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `null`<br> |
| `Camera` | `setRotation` | `handle` : object<br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br> | `null`<br> |
| `Camera` | `setTransformation` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br> | `null`<br> |
| `Camera` | `setTransformationAndLensProps` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null`<br> |
| `Camera` | `setTransformationAndLensPropsExt` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`focalDistance` : double <br>`zoom` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`k3` : double <br>`p1` : double <br>`p2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br>`overscan` : double <br> | `null`<br> |
#### Perspective
Syntax: *Pixera.Direct.Perspective.(method)*
| Class Name | Method Name | Parameters | Return Values |
| --- | --- | --- | --- |
| `Perspective` | `setTransformation` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br> | `null`<br> |
| `Perspective` | `setTransformationAndLensProps` | `handle` : object<br>`xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null`<br> |

## Unreal
Syntax: *Pixera.Unreal.(function)*
### Functions
| Name | Parameters | Return Values |
| --- | --- | --- |
| `getSupportedUnrealPluginVersion` | None | `int`<br> |

