
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
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getApiRevision` | None | `int` : int <br> |
| Function | | `getHasFunction` | `functionName` : string <br> | `bool` : bool <br> |
| Function | | `outputDebug` | `message` : string <br> | `string` : string <br> |
| Function | | `getLicenseJson` | None | `string` : string <br> |
| Function | | `getCurrentTime` | None | `double` : double <br> |
| Function | | `getCurrentTimeAsString` | None | `string` : string <br> |
| Function | | `noop` | None | `null` : null <br> |
| Function | | `requestCallback` | `functionName` : string <br> | `null` : null <br> |
| Function | | `readFileString` | `path` : string <br> | `string` : string <br> |
| Function | | `writeFileString` | `path` : string <br>`fileStr` : string <br> | `null` : null <br> |
| Function | | `getAccessRecipe` | `hdlPath` : string <br> | `string` : string <br> |
| Function | | `pollMonitoring` | None | `string` : string <br> |
| Function | | `unsubscribeMonitoringSubject` | `subject` : string <br> | `bool` : bool <br> |
| Function | | `subscribeMonitoringSubject` | `subject` : string <br> | `bool` : bool <br> |
| Function | | `setMonitoringEventMode` | `mode` : string <br> | `bool` : bool <br> |
| Function | | `monitoringEvent` | `eventDescription` : string <br> | `null` : null <br> |
| Function | | `setShowContextInReplies` | `doShow` : bool <br> | `bool` : bool <br> |
| Function | | `setMonitoringHasDelimiter` | `hasDelimiter` : bool <br> | `bool` : bool <br> |
| Function | | `runJsScript` | `jsFunction` : string <br>`jsCode` : string <br> | `string` : string <br> |
| Function | | `dynamicRebuildFromJsonDescription` | `deviceName` : string <br>`jsonDescription` : string <br>`folder` : string <br> | `null` : null <br> |

## Network
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getConveyor` | `conveyorName` : string <br> | `handle` : handle <br> |
| Class | | `Conveyor` | | |
| | Method | `sendString` | `str` : string <br> | `null` : null <br> |

## Compound
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `setTransportModeOnTimelineAtIndex` | `index` : int <br>`mode` : int <br> | `bool` : bool <br> |
| Function | | `setTransportModeOnTimeline` | `timelineName` : string <br>`mode` : int <br> | `null` : null <br> |
| Function | | `toggleTransport` | `timelineName` : string <br> | `null` : null <br> |
| Function | | `getTransportModeOnTimeline` | `timelineName` : string <br> | `int` : int <br> |
| Function | | `setOpacityOnTimeline` | `timelineName` : string <br>`opacity` : double <br> | `null` : null <br> |
| Function | | `getOpacityOnTimeline` | `timelineName` : string <br> | `double` : double <br> |
| Function | | `startFirstTimeline` | None | `null` : null <br> |
| Function | | `pauseFirstTimeline` | None | `null` : null <br> |
| Function | | `stopFirstTimeline` | None | `null` : null <br> |
| Function | | `setPosValue` | `val` : double <br> | `null` : null <br> |
| Function | | `setPosValueXY` | `valX` : double <br>`valY` : double <br> | `null` : null <br> |
| Function | | `setParamValue` | `path` : string <br>`value` : double <br> | `null` : null <br> |
| Function | | `applyCueAtIndexOnTimelineAtIndex` | `cueIndex` : int <br>`timelineIndex` : int <br> | `null` : null <br> |
| Function | | `applyCueNumberOnTimelineAtIndex` | `cueNumber` : int <br>`timelineIndex` : int <br> | `null` : null <br> |
| Function | | `applyCueNumberOnTimeline` | `timelineName` : string <br>`cueNumber` : int <br> | `null` : null <br> |
| Function | | `applyCueOnTimeline` | `timelineName` : string <br>`cueName` : string <br> | `null` : null <br> |
| Function | | `addResourceToFolder` | `namePath` : string <br>`filePath` : string <br> | `handle` : handle <br> |
| Function | | `assignResourceToLayer` | `resourcePath` : string <br>`layerPath` : string <br> | `null` : null <br> |
| Function | | `refreshResource` | `resourcePath` : string <br> | `null` : null <br> |
| Function | | `setTransportModeOnLayer` | `layerPath` : string <br>`mode` : int <br>`loop` : bool <br> | `null` : null <br> |
| Function | | `getTransportModeOnLayer` | `layerPath` : string <br> | `int` : int <br> |
| Function | | `getResourceAssignedToLayer` | `layerPath` : string <br> | `string` : string <br> |
| Function | | `assignResourceToClipAtTimeByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`time` : double <br> | `null` : null <br> |
| Function | | `assignResourceToClipAtHMSFStringByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`hmsf` : string <br> | `null` : null <br> |
| Function | | `assignResourceToClipAtHMSFByDmxId` | `layerPath` : string <br>`dmxFolderId` : int <br>`dmxFileId` : int <br>`h` : int <br>`m` : int <br>`s` : int <br>`f` : int <br> | `null` : null <br> |
| Function | | `setCurrentTimeOfTimeline` | `timelineName` : string <br>`time` : int <br> | `null` : null <br> |
| Function | | `setCurrentTimeOfTimelineInSeconds` | `timelineName` : string <br>`time` : double <br> | `null` : null <br> |
| Function | | `setCurrentTimeAndTransportModeOfTimelineInSeconds` | `timelineName` : string <br>`time` : double <br>`mode` : int <br> | `null` : null <br> |
| Function | | `getFpsOfTimeline` | `timelineName` : string <br> | `double` : double <br> |
| Function | | `getCurrentTimeOfTimeline` | `timelineName` : string <br> | `int` : int <br> |
| Function | | `getCurrentTimeOfTimelineInSeconds` | `timelineName` : string <br> | `double` : double <br> |
| Function | | `getCurrentHMSFOfTimeline` | `timelineName` : string <br> | `string` : string <br> |
| Function | | `getCurrentCountdownOfTimeline` | `timelineName` : string <br> | `int` : int <br> |
| Function | | `getCurrentCountdownHMSFOfTimeline` | `timelineName` : string <br> | `string` : string <br> |
| Function | | `startOpacityAnimationOfTimeline` | `timelineName` : string <br>`fadeIn` : bool <br>`fullFadeDuration` : double <br> | `null` : null <br> |
| Function | | `createClipOnLayerAtTimeWithResource` | `layerPath` : string <br>`time` : double <br>`resourcePath` : string <br> | `null` : null <br> |
| Function | | `removeClipOnLayerWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `null` : null <br> |
| Function | | `removeAllClipsOnLayer` | `layerPath` : string <br> | `null` : null <br> |
| Function | | `getClipDurationInSecondsWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `double` : double <br> |
| Function | | `getClipDurationInFramesWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `int` : int <br> |
| Function | | `getClipTimeInSecondsWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `double` : double <br> |
| Function | | `getClipEndTimeInSecondsWithIndex` | `layerPath` : string <br>`clipIndex` : int <br> | `double` : double <br> |
| Function | | `getResourceDurationInSeconds` | `resourcePath` : string <br> | `double` : double <br> |
| Function | | `getParamValue` | `path` : string <br> | `double` : double <br> |
| Function | | `setTimecodeInput` | `hour` : int <br>`minute` : int <br>`second` : int <br>`frame` : int <br>`elapsedTime` : double <br>`running` : bool <br>`freshMode` : int <br>`stateToken` : int <br>`format` : int <br> | `double` : double <br> |
| Function | | `takeOverAllClients` | None | `null` : null <br> |
| Function | | `setPauseSmpteInput` | `doPause` : bool <br> | `null` : null <br> |

## Session
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `closeApp` | `saveProject` : bool <br> | `null` : null <br> |
| Function | | `loadProject` | `path` : string <br> | `null` : null <br> |
| Function | | `saveProject` | None | `null` : null <br> |
| Function | | `saveProjectAs` | `path` : string <br> | `null` : null <br> |
| Function | | `getProjectName` | None | `string` : string <br> |
| Function | | `setProjectName` | `name` : string <br> | `null` : null <br> |
| Function | | `getProjectDirectory` | None | `string` : string <br> |
| Function | | `getControlMultiUserSessionName` | None | `string` : string <br> |
| Function | | `shutdownSystem` | `mode` : optional<int> <br> | `null` : null <br> |
| Function | | `getLiveSystemIps` | None | `string[]` : string[] <br> |
| Function | | `getLiveSystemState` | `ip` : string <br> | `string` : string <br> |
| Function | | `liveSystemStateChange` | `ip` : string <br>`state` : string <br> | `null` : null <br> |
| Function | | `shutdownLiveSystem` | `ip` : string <br>`mode` : optional<int> <br> | `null` : null <br> |
| Function | | `wakeLiveSystem` | `ip` : string <br> | `string` : string <br> |
| Function | | `getLiveSystemMacAddress` | `ip` : string <br> | `string` : string <br> |
| Function | | `startLiveSystem` | `ip` : string <br> | `null` : null <br> |
| Function | | `startLiveSystems` | None | `null` : null <br> |
| Function | | `stopLiveSystem` | `ip` : string <br> | `null` : null <br> |
| Function | | `stopLiveSystems` | None | `null` : null <br> |
| Function | | `restartLiveSystem` | `ip` : string <br> | `null` : null <br> |
| Function | | `restartLiveSystems` | None | `null` : null <br> |
| Function | | `remoteSystemStateChange` | `ip` : string <br>`state` : string <br> | `null` : null <br> |
| Function | | `getRemoteSystemIps` | None | `string[]` : string[] <br> |
| Function | | `getRemoteSystemState` | `ip` : string <br> | `string` : string <br> |
| Function | | `setVideoStreamActiveState` | `ip` : string <br>`device` : string <br>`isActive` : bool <br> | `null` : null <br> |
| Function | | `getVideoStreamActiveState` | `ip` : string <br>`device` : string <br> | `bool` : bool <br> |
| Function | | `getDefaultClipDurationsAsJsonString` | None | `string` : string <br> |

## LiveSystems
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getLiveSystems` | None | `handle[]` : handle[] <br> |
| Function | | `liveSystemNotAvailable` | `reason` : int <br>`system` : handle <br> | `null` : null <br> |
| Function | | `getMultiUserMembers` | None | `handle[]` : handle[] <br> |
| Class | | `MultiUserMember` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `getIp` | None | `string` : string <br> |
| | Method | `getState` | None | `string` : string <br> |
| | Method | `getPerformanceMonitoringValuesJson` | None | `string` : string <br> |
| | Method | `getPerformanceMonitoringValuesJsonEx` | `filter` : string <br> | `string` : string <br> |
| | Method | `resetCumulativePerformanceMonitoringValues` | None | `null` : null <br> |
| | Method | `ensureFileDistribution` | `includeNotUsedYet` : bool <br> | `null` : null <br> |
| | Method | `shutDown` | `mode` : int <br> | `null` : null <br> |
| | Method | `wakeUp` | None | `string` : string <br> |
| | Method | `getMacAddress` | None | `string` : string <br> |
| | Method | `resetEngine` | None | `null` : null <br> |
| | Method | `restartEngine` | None | `null` : null <br> |
| | Method | `startEngine` | None | `null` : null <br> |
| | Method | `closeEngine` | None | `null` : null <br> |
| | Method | `triggerBackup` | `applyControlCommand` : optional<bool> <br> | `null` : null <br> |
| | Method | `getStructureJson` | None | `string` : string <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| Class | | `LiveSystem` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `getIp` | None | `string` : string <br> |
| | Method | `getState` | None | `string` : string <br> |
| | Method | `setBackupRole` | `role` : int <br> | `null` : null <br> |
| | Method | `getBackupRole` | None | `int` : int <br> |
| | Method | `getPerformanceMonitoringValuesJson` | None | `string` : string <br> |
| | Method | `getPerformanceMonitoringValuesJsonEx` | `filter` : string <br> | `string` : string <br> |
| | Method | `resetCumulativePerformanceMonitoringValues` | None | `null` : null <br> |
| | Method | `moveMappingsToOutputs` | `hdlSrc` : handle <br>`outputIdPathMapStr` : string <br> | `null` : null <br> |
| | Method | `clearExportedMappings` | `path` : string <br>`onlyServicePath` : bool <br> | `null` : null <br> |
| | Method | `exportMappings` | `path` : string <br> | `null` : null <br> |
| | Method | `importMappings` | `path` : string <br>`outputIdPathMapStr` : string <br> | `null` : null <br> |
| | Method | `exportMappingsDirectly` | `path` : string <br> | `null` : null <br> |
| | Method | `importMappingsDirectly` | `path` : string <br>`outputIdPathMapStr` : string <br> | `null` : null <br> |
| | Method | `exportMappingsToLiveSystemPath` | `parentPath` : string <br> | `null` : null <br> |
| | Method | `importMappingsFromLiveSystemPath` | `parentPath` : string <br> | `null` : null <br> |
| | Method | `clearExportedMappingsAtLiveSystemPath` | `path` : string <br> | `null` : null <br> |
| | Method | `ensureFileDistribution` | `includeNotUsedYet` : bool <br> | `null` : null <br> |
| | Method | `shutDown` | `mode` : int <br> | `null` : null <br> |
| | Method | `wakeUp` | None | `string` : string <br> |
| | Method | `getMacAddress` | None | `string` : string <br> |
| | Method | `getGraphicsDevices` | None | `handle[]` : handle[] <br> |
| | Method | `getEnabledOutputs` | None | `handle[]` : handle[] <br> |
| | Method | `getAllOutputs` | None | `handle[]` : handle[] <br> |
| | Method | `getVideoStreamOutputs` | None | `handle[]` : handle[] <br> |
| | Method | `resetEngine` | None | `null` : null <br> |
| | Method | `restartEngine` | None | `null` : null <br> |
| | Method | `startEngine` | None | `null` : null <br> |
| | Method | `closeEngine` | None | `null` : null <br> |
| | Method | `setAudioMasterVolume` | `channel` : int <br>`volume` : double <br> | `null` : null <br> |
| | Method | `getAudioMasterVolume` | `channel` : int <br> | `double` : double <br> |
| | Method | `setAudioMasterMute` | `channel` : int <br>`state` : bool <br> | `null` : null <br> |
| | Method | `getAudioMasterMute` | `channel` : int <br> | `bool` : bool <br> |
| | Method | `setAudioTimecodeInput` | `channel` : int <br>`state` : bool <br> | `null` : null <br> |
| | Method | `triggerBackup` | `applyControlCommand` : optional<bool> <br> | `null` : null <br> |
| | Method | `getStructureJson` | None | `string` : string <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `GraphicsDevice` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `getEnabledOutputs` | None | `handle[]` : handle[] <br> |
| | Method | `getAllOutputs` | None | `handle[]` : handle[] <br> |
| Class | | `Output` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setActive` | `active` : bool <br> | `null` : null <br> |
| | Method | `getActive` | None | `bool` : bool <br> |
| | Method | `setIdentify` | `state` : bool <br> | `null` : null <br> |
| | Method | `getIdentify` | None | `bool` : bool <br> |
| | Method | `getAssignedScreens` | None | `handle[]` : handle[] <br> |
| | Method | `getAssignedProjectors` | None | `handle[]` : handle[] <br> |
| | Method | `getEnabled` | None | `bool` : bool <br> |
| | Method | `getForPreview` | None | `bool` : bool <br> |
| Class | | `VideoStream` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setActive` | `active` : bool <br> | `null` : null <br> |
| | Method | `getActive` | None | `bool` : bool <br> |

## Settings
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |

## Screens
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getScreenWithName` | `name` : string <br> | `handle` : handle <br> |
| Function | | `setNamedScreenPosition` | `name` : string <br>`xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null` : null <br> |
| Function | | `getScreens` | None | `handle[]` : handle[] <br> |
| Function | | `getScreenNames` | None | `string[]` : string[] <br> |
| Function | | `getFirstTimelineWithHomeScreen` | `screenName` : string <br> | `handle` : handle <br> |
| Function | | `getStudioCameras` | None | `handle[]` : handle[] <br> |
| Class | | `Screen` | | |
| | Method | `getId` | None | `double` : double <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getPosition` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getRotation` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setScale` | `xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getScale` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setPosRot` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool` : bool <br> |
| | Method | `setPosRotScale` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getPersepective` | None | `handle` : handle <br> |
| | Method | `snapPerspectiveCornersToScreen` | `mode` : int <br> | `null` : null <br> |
| | Method | `setPerspectivePosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool` : bool <br> |
| | Method | `setPerspectivePositionWithLookAt` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getPerspectivePosition` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setPerspectiveRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getPerspectiveRotation` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setCameraPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool` : bool <br> |
| | Method | `setCameraPositionWithLookAt` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getCameraPosition` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setCameraRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getCameraRotation` | None | `ScreenPosValues` : ScreenPosValues <br> |
| | Method | `setContentSamplingFrustumBase` | `x` : double <br>`y` : double <br>`width` : double <br>`height` : double <br>`rotation` : double <br>`originScreenId` : double <br> | `null` : null <br> |
| | Method | `runCalibration` | `mode` : string <br>`diff` : string <br> | `null` : null <br> |
| | Method | `editCalibration` | `diff` : string <br> | `null` : null <br> |
| | Method | `resetWarpFile` | `diff` : string <br> | `null` : null <br> |
| | Method | `loadWarpFile` | `filePath` : string <br> | `null` : null <br> |
| | Method | `loadWarpFileWithDiff` | `filePath` : string <br>`diff` : string <br> | `null` : null <br> |
| | Method | `addWarpFile` | `filePath` : string <br> | `null` : null <br> |
| | Method | `addWarpFileWithDiff` | `filePath` : string <br>`diff` : string <br> | `null` : null <br> |
| | Method | `loadColorCalibration` | `calibrationName` : string <br> | `null` : null <br> |
| | Method | `runColorCalibration` | None | `null` : null <br> |
| | Method | `setIsVisible` | `isVisible` : bool <br> | `null` : null <br> |
| | Method | `getIsVisible` | None | `bool` : bool <br> |
| | Method | `setIsProjectable` | `isProjectable` : bool <br> | `null` : null <br> |
| | Method | `getIsProjectable` | None | `bool` : bool <br> |
| | Method | `triggerRefreshMapping` | None | `null` : null <br> |
| | Method | `resetAllColorCorrections` | None | `null` : null <br> |
| | Method | `setColorCorrectionWithPath` | `path` : string <br>`value` : float <br> | `null` : null <br> |
| | Method | `getColorCorrectionWithPath` | `path` : string <br> | `float` : float <br> |
| | Method | `setColorCorrectionAsJsonString` | `colorCorrection` : string <br> | `null` : null <br> |
| | Method | `getColorCorrectionAsJsonString` | None | `string` : string <br> |
| | Method | `getOutput` | None | `handle[]` : handle[] <br> |
| | Method | `setBlackout` | `isActive` : bool <br> | `null` : null <br> |
| | Method | `getBlackout` | None | `bool` : bool <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `StudioCamera` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null` : null <br> |
| | Method | `getPosition` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `double[]` : double[] <br> |
| | Method | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null` : null <br> |
| | Method | `getRotation` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `double[]` : double[] <br> |
| | Method | `setTransformation` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`fov` : optional<double> <br>`aspectRatio` : optional<double> <br> | `null` : null <br> |
| | Method | `setTransformationAndLensProps` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null` : null <br> |
| | Method | `setTransformationAndLensPropsExt` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`focalDistance` : double <br>`zoom` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`k3` : double <br>`p1` : double <br>`p2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br>`overscan` : double <br> | `null` : null <br> |
| | Method | `setTrackingInputPause` | `pause` : bool <br> | `null` : null <br> |
| | Method | `getTrackingInputPause` | None | `bool` : bool <br> |
| | Method | `setUsePositionPropertiesFromTracking` | `pause` : bool <br> | `null` : null <br> |
| | Method | `getUsePositionPropertiesFromTracking` | None | `bool` : bool <br> |
| | Method | `setUseRotationPropertiesFromTracking` | `pause` : bool <br> | `null` : null <br> |
| | Method | `getUseRotationPropertiesFromTracking` | None | `bool` : bool <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `Perspective` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setTransformation` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`fov` : optional<double> <br>`aspectRatio` : optional<double> <br> | `null` : null <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |

## Projectors
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getProjectorWithName` | `name` : string <br> | `handle` : handle <br> |
| Function | | `getProjectors` | None | `handle[]` : handle[] <br> |
| Function | | `getProjectorNames` | None | `string[]` : string[] <br> |
| Class | | `Projector` | | |
| | Method | `getPosition` | None | `ProjectorPosValues` : ProjectorPosValues <br> |
| | Method | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getRotation` | None | `ProjectorPosValues` : ProjectorPosValues <br> |
| | Method | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `bool` : bool <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `activateScreenMapping` | `screenId` : double <br>`isActive` : bool <br> | `null` : null <br> |
| | Method | `setBlackout` | `isActive` : bool <br> | `null` : null <br> |
| | Method | `getBlackout` | None | `bool` : bool <br> |
| | Method | `setSoftedgeVisible` | `screenName` : string <br>`visible` : bool <br> | `null` : null <br> |
| | Method | `resetAllColorCorrections` | None | `null` : null <br> |
| | Method | `setColorCorrectionWithPath` | `path` : string <br>`value` : float <br> | `null` : null <br> |
| | Method | `getColorCorrectionWithPath` | `path` : string <br> | `float` : float <br> |
| | Method | `setColorCorrectionAsJsonString` | `colorCorrection` : string <br> | `null` : null <br> |
| | Method | `getColorCorrectionAsJsonString` | None | `string` : string <br> |
| | Method | `getOutput` | None | `handle` : handle <br> |
| | Method | `setOutput` | `outputHandle` : handle <br> | `null` : null <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |

## Resources
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getResources` | None | `handle[]` : handle[] <br> |
| Function | | `getResourceFolderWithNamePath` | `namePath` : string <br> | `handle` : handle <br> |
| Function | | `getResourceFolders` | None | `handle[]` : handle[] <br> |
| Function | | `getTranscodingFolders` | None | `handle[]` : handle[] <br> |
| Function | | `getJsonDescrip` | None | `string` : string <br> |
| Class | | `ResourceFolder` | | |
| | Method | `ref` | None | `handle` : handle <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setName` | `name` : string <br> | `null` : null <br> |
| | Method | `getResourceFolders` | None | `handle[]` : handle[] <br> |
| | Method | `getResources` | None | `handle[]` : handle[] <br> |
| | Method | `getResourceAtIndex` | `index` : int <br> | `handle` : handle <br> |
| | Method | `addResource` | `path` : string <br> | `handle` : handle <br> |
| | Method | `addResourcesFromDirectory` | `path` : string <br>`removeOthers` : bool <br>`checkRedundancy` : bool <br> | `handle[]` : handle[] <br> |
| | Method | `addResourcesFromDirectoryRemoveAssets` | `path` : string <br>`removeOthers` : bool <br>`checkRedundancy` : bool <br> | `handle[]` : handle[] <br> |
| | Method | `addInternalResource` | `signature` : string <br>`resKind` : int <br> | `handle` : handle <br> |
| | Method | `createFoldersFrom` | `path` : string <br> | `null` : null <br> |
| | Method | `refreshResources` | None | `null` : null <br> |
| | Method | `moveResourceToThis` | `id` : double <br> | `null` : null <br> |
| | Method | `removeThis` | None | `null` : null <br> |
| | Method | `removeThisIncludingAssets` | None | `null` : null <br> |
| | Method | `removeAllContents` | None | `null` : null <br> |
| | Method | `removeAllContentsIncludingAssets` | None | `null` : null <br> |
| | Method | `deleteAllContentsAssetsFromLiveSystem` | `apEntityLiveSystemHandle` : handle <br> | `null` : null <br> |
| | Method | `resetDistributionTargets` | None | `null` : null <br> |
| | Method | `changeDistributionTarget` | `apEntityLiveSystemHandle` : handle <br>`shouldDistribute` : bool <br> | `null` : null <br> |
| | Method | `replaceResourcesByString` | `searchString` : string <br>`replaceString` : string <br>`path` : string <br> | `null` : null <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| | Method | `getDmxId` | None | `int` : int <br> |
| | Method | `getCombinedDmxId` | None | `int` : int <br> |
| | Method | `setDmxId` | `id` : int <br> | `null` : null <br> |
| Class | | `TranscodingFolder` | | |
| | Method | `getUsedTranscodingPreset` | None | `string` : string <br> |
| | Method | `setUsedTranscodingPreset` | `preset` : string <br> | `null` : null <br> |
| | Method | `getTranscodeAutomatically` | None | `bool` : bool <br> |
| | Method | `setTranscodeAutomatically` | `autoTranscode` : bool <br> | `null` : null <br> |
| | Method | `getUseRxCacheAsDestination` | None | `bool` : bool <br> |
| | Method | `setRxCacheAsDestination` | `useRxCache` : bool <br> | `null` : null <br> |
| | Method | `getDestinationDirectory` | None | `string` : string <br> |
| | Method | `setDestinationDirectory` | `path` : string <br> | `null` : null <br> |
| Class | | `Resource` | | |
| | Method | `ref` | None | `handle` : handle <br> |
| | Method | `removeThis` | None | `null` : null <br> |
| | Method | `deleteFilesOnSystems` | None | `null` : null <br> |
| | Method | `removeThisIncludingAssets` | None | `null` : null <br> |
| | Method | `deleteAssetFromLiveSystem` | `apEntityLiveSystemHandle` : handle <br> | `null` : null <br> |
| | Method | `resetDistributionTargets` | None | `null` : null <br> |
| | Method | `changeDistributionTarget` | `apEntityLiveSystemHandle` : handle <br>`shouldDistribute` : bool <br> | `null` : null <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setName` | `name` : string <br> | `null` : null <br> |
| | Method | `getFps` | None | `double` : double <br> |
| | Method | `getResolution` | None | `double[]` : double[] <br> |
| | Method | `getIsActive` | None | `bool` : bool <br> |
| | Method | `getVideoStreamModes` | None | `string[]` : string[] <br> |
| | Method | `setVideoStreamMode` | `index` : int <br> | `null` : null <br> |
| | Method | `getId` | None | `double` : double <br> |
| | Method | `getDuration` | None | `double` : double <br> |
| | Method | `getType` | None | `string` : string <br> |
| | Method | `setCurrentVersion` | `version` : string <br> | `null` : null <br> |
| | Method | `getCurrentVersion` | None | `string` : string <br> |
| | Method | `getVersions` | None | `string[]` : string[] <br> |
| | Method | `getVersionSuffix` | None | `string[]` : string[] <br> |
| | Method | `rescanVersions` | None | `null` : null <br> |
| | Method | `getThumbnailAsBase64` | None | `string` : string <br> |
| | Method | `getHasPendingTransfer` | None | `bool` : bool <br> |
| | Method | `getIsInUse` | None | `double` : double <br> |
| | Method | `getLastUsageBeginTime` | None | `double` : double <br> |
| | Method | `getLastUsageBeginTimeAsString` | None | `string` : string <br> |
| | Method | `getLastUsageEndTime` | None | `double` : double <br> |
| | Method | `getLastUsageEndTimeAsString` | None | `string` : string <br> |
| | Method | `getFilePath` | None | `string` : string <br> |
| | Method | `setText` | `text` : string <br> | `null` : null <br> |
| | Method | `getText` | None | `string` : string <br> |
| | Method | `setFontWithName` | `fontName` : string <br> | `bool` : bool <br> |
| | Method | `getFontName` | None | `string` : string <br> |
| | Method | `setFontWithPath` | `fontPath` : string <br> | `bool` : bool <br> |
| | Method | `setHorizontalTextAlignment` | `textAlignment` : int <br> | `bool` : bool <br> |
| | Method | `getHorizontalTextAlignment` | None | `int` : int <br> |
| | Method | `setVerticalTextAlignment` | `textAlignment` : int <br> | `bool` : bool <br> |
| | Method | `getVerticalTextAlignment` | None | `int` : int <br> |
| | Method | `setLineHeight` | `lineHeight` : double <br> | `bool` : bool <br> |
| | Method | `getLineHeight` | None | `double` : double <br> |
| | Method | `getTextMeasurementsWidthAndHeight` | None | `int[]` : int[] <br> |
| | Method | `setUrl` | `url` : string <br> | `null` : null <br> |
| | Method | `getUrl` | None | `string` : string <br> |
| | Method | `setColorTransformPath` | `colorTransformPath` : string <br> | `null` : null <br> |
| | Method | `getColorTransformPath` | None | `string` : string <br> |
| | Method | `clearColorTransformPath` | None | `null` : null <br> |
| | Method | `refresh` | `text` : string <br> | `null` : null <br> |
| | Method | `distribute` | None | `null` : null <br> |
| | Method | `getDmxId` | None | `int` : int <br> |
| | Method | `setDmxId` | `id` : int <br> | `null` : null <br> |
| | Method | `removeMultiresourceIndex` | `index` : int <br> | `null` : null <br> |
| | Method | `addMultiresourceItem` | `id` : double <br> | `null` : null <br> |
| | Method | `getMultiresourceItems` | None | `handle[]` : handle[] <br> |
| | Method | `replaceMultiresourceItemByIndex` | `index` : int <br>`id` : double <br> | `null` : null <br> |
| | Method | `setMultiresourceResolution` | `width` : int <br>`height` : int <br> | `null` : null <br> |
| | Method | `setMultiresourceItemSizebyIndex` | `index` : int <br>`width` : double <br>`height` : double <br> | `null` : null <br> |
| | Method | `setMultiresourceItemPositionbyIndex` | `index` : int <br>`x` : double <br>`y` : double <br> | `null` : null <br> |
| | Method | `setUseGradient` | `useGradient` : bool <br> | `null` : null <br> |
| | Method | `getUseGradient` | None | `bool` : bool <br> |
| | Method | `setColors` | `argbCols` : uint[] <br>`positions` : double[] <br>`colNames` : string[] <br>`useGradient` : optional<bool> <br> | `null` : null <br> |
| | Method | `setColorAtIndex` | `index` : int <br>`red` : int <br>`green` : int <br>`blue` : int <br>`alpha` : int <br>`position` : double <br>`name` : string <br>`useGradient` : optional<bool> <br> | `null` : null <br> |
| | Method | `getColorAtIndex` | `colorIndex` : int <br> | `int` : int <br> |
| | Method | `getColorPositionAtIndex` | `colorIndex` : int <br> | `double` : double <br> |
| | Method | `launchVirtualWorld` | `action` : string <br> | `null` : null <br> |
| | Method | `getUnrealWorld` | None | `handle` : handle <br> |
| | Method | `setMultiResourceItemRestrictedServiceIps` | `itemIndex` : int <br>`ipAdresses` : string[] <br> | `null` : null <br> |
| | Method | `getMultiResourceItemRestrictedServiceIps` | `itemIndex` : int <br> | `string[]` : string[] <br> |
| | Method | `replace` | `path` : string <br> | `null` : null <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| | Method | `transcodeWithExisitngPreset` | `presetName` : string <br>`useRxCache` : bool <br>`destinationPath` : string <br>`startFrame` : int <br>`endFrame` : int <br>`serviceId` : uint <br> | `null` : null <br> |
| | Method | `transcodeWithSettings` | `settings` : string <br>`useRxCache` : bool <br>`destinationPath` : string <br>`startFrame` : int <br>`endFrame` : int <br>`serviceId` : uint <br> | `null` : null <br> |
| | Method | `moveToTranscodingFolder` | `folderPath` : string <br> | `null` : null <br> |
| Class | | `UnrealWorld` | | |
| | Method | `getLevelNames` | None | `string[]` : string[] <br> |
| | Method | `loadLevel` | `levelName` : string <br> | `null` : null <br> |
| | Method | `getEventTriggerNames` | None | `string[]` : string[] <br> |
| | Method | `triggerEventByName` | `triggerName` : string <br> | `null` : null <br> |
| | Method | `createNDisplayConfig` | None | `null` : null <br> |
| | Method | `runUnreal` | None | `null` : null <br> |
| | Method | `killUnreal` | None | `null` : null <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |

## Timelines
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getTimelineAtIndex` | `index` : int <br> | `handle` : handle <br> |
| Function | | `getTimelineFromName` | `name` : string <br> | `handle` : handle <br> |
| Function | | `getTimelines` | None | `handle[]` : handle[] <br> |
| Function | | `getTimelineNames` | None | `string[]` : string[] <br> |
| Function | | `getTimelinesSelected` | None | `handle[]` : handle[] <br> |
| Function | | `createTimeline` | None | `handle` : handle <br> |
| Function | | `getNodeFromId` | `id` : double <br> | `handle` : handle <br> |
| Class | | `Timeline` | | |
| | Method | `ref` | None | `handle` : handle <br> |
| | Method | `removeThis` | None | `null` : null <br> |
| | Method | `duplicateThis` | `withoutClipsCues` : optional<bool> <br> | `handle` : handle <br> |
| | Method | `selectThis` | None | `null` : null <br> |
| | Method | `getZoomFactor` | None | `double` : double <br> |
| | Method | `setZoomFactor` | `zoomFactor` : double <br> | `null` : null <br> |
| | Method | `getVerticalScrollOffset` | None | `int` : int <br> |
| | Method | `setVerticalScrollOffset` | `offset` : int <br> | `null` : null <br> |
| | Method | `getHorizontalScrollOffset` | None | `int` : int <br> |
| | Method | `setHorizontalScrollOffset` | `offset` : int <br> | `null` : null <br> |
| | Method | `moveInRenderOrder` | `moveDown` : bool <br> | `null` : null <br> |
| | Method | `getLayers` | None | `handle[]` : handle[] <br> |
| | Method | `getLayerNames` | None | `string[]` : string[] <br> |
| | Method | `getLayersSelected` | None | `handle[]` : handle[] <br> |
| | Method | `selectLayerByIndex` | `index` : int <br> | `null` : null <br> |
| | Method | `selectLayerByNames` | `layerNames` : string[] <br> | `null` : null <br> |
| | Method | `getLayerAtIndex` | `index` : int <br> | `handle` : handle <br> |
| | Method | `createLayer` | None | `handle` : handle <br> |
| | Method | `getCueInfosAsJsonString` | None | `string` : string <br> |
| | Method | `getCues` | None | `handle[]` : handle[] <br> |
| | Method | `getCueNames` | None | `string[]` : string[] <br> |
| | Method | `getCueAtIndex` | `index` : int <br> | `handle` : handle <br> |
| | Method | `getCueFromName` | `name` : string <br> | `handle` : handle <br> |
| | Method | `getCueFromNumber` | `number` : int <br> | `handle` : handle <br> |
| | Method | `applyCueWithName` | `name` : string <br> | `null` : null <br> |
| | Method | `applyCueWithNumber` | `number` : int <br> | `null` : null <br> |
| | Method | `createCue` | `name` : string <br>`timeInFrames` : double <br>`operation` : int <br> | `handle` : handle <br> |
| | Method | `removeCues` | None | `null` : null <br> |
| | Method | `createPauseCueBeforeSelectedClips` | None | `null` : null <br> |
| | Method | `play` | None | `null` : null <br> |
| | Method | `pause` | None | `null` : null <br> |
| | Method | `stop` | None | `null` : null <br> |
| | Method | `toggleTransport` | None | `null` : null <br> |
| | Method | `store` | None | `null` : null <br> |
| | Method | `reset` | None | `null` : null <br> |
| | Method | `getAttributes` | None | `TimelineAttributes` : TimelineAttributes <br> |
| | Method | `setCurrentFrame` | `time` : int <br> | `bool` : bool <br> |
| | Method | `setCurrentTime` | `time` : int <br> | `null` : null <br> |
| | Method | `getCurrentTime` | None | `int` : int <br> |
| | Method | `scrubCurrentTime` | `frames` : int <br> | `null` : null <br> |
| | Method | `CurrentTime` | `time` : int <br>`doSet` : bool <br> | `int` : int <br> |
| | Method | `getCurrentHMSF` | None | `string` : string <br> |
| | Method | `setTransportMode` | `mode` : int <br> | `bool` : bool <br> |
| | Method | `getTransportMode` | None | `int` : int <br> |
| | Method | `setTimecodeInput` | `hour` : int <br>`minute` : int <br>`second` : int <br>`frame` : int <br>`elapsedTime` : double <br>`running` : bool <br>`freshMode` : int <br>`stateToken` : int <br>`format` : int <br> | `double` : double <br> |
| | Method | `getFps` | None | `double` : double <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setName` | `name` : string <br> | `null` : null <br> |
| | Method | `moveToNextCue` | None | `null` : null <br> |
| | Method | `moveToNextCueIgnoreProperties` | None | `null` : null <br> |
| | Method | `getCueNext` | None | `handle` : handle <br> |
| | Method | `moveToPreviousCue` | None | `null` : null <br> |
| | Method | `moveToPreviousCueIgnoreProperties` | None | `null` : null <br> |
| | Method | `getCuePrevious` | None | `handle` : handle <br> |
| | Method | `ignoreNextCue` | None | `null` : null <br> |
| | Method | `ignoreNextCueWithOperation` | `cueOperation` : int <br> | `null` : null <br> |
| | Method | `blendToTime` | `goalTime` : double <br>`blendDuration` : double <br>`preloadDelayInMilliseconds` : optional<int> <br> | `null` : null <br> |
| | Method | `blendToTimeWithTransportMode` | `goalTime` : double <br>`blendDuration` : double <br>`transportMode` : int <br>`preloadDelayInMilliseconds` : optional<int> <br> | `null` : null <br> |
| | Method | `setBlendToTimeMode` | `mode` : int <br> | `bool` : bool <br> |
| | Method | `setSpeedFactor` | `factor` : double <br> | `null` : null <br> |
| | Method | `getSpeedFactor` | None | `double` : double <br> |
| | Method | `setOpacity` | `value` : double <br> | `null` : null <br> |
| | Method | `getOpacity` | None | `double` : double <br> |
| | Method | `startOpacityAnimation` | `fadeIn` : bool <br>`durationFrames` : double <br> | `null` : null <br> |
| | Method | `setSmpteMode` | `mode` : int <br> | `null` : null <br> |
| | Method | `getSmpteMode` | None | `int` : int <br> |
| | Method | `storeRecordedValues` | None | `null` : null <br> |
| | Method | `setSmpteInputBehaviour` | `mode` : int <br> | `null` : null <br> |
| | Method | `getSmpteInputBehaviour` | None | `int` : int <br> |
| | Method | `setSmpteOffset` | `time` : double <br> | `null` : null <br> |
| | Method | `getSmpteOffset` | None | `double` : double <br> |
| | Method | `resetRecordedValues` | None | `null` : null <br> |
| | Method | `getTimelineInfosAsJsonString` | None | `string` : string <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `Layer` | | |
| | Method | `ref` | None | `handle` : handle <br> |
| | Method | `removeThis` | None | `null` : null <br> |
| | Method | `getNodes` | None | `handle[]` : handle[] <br> |
| | Method | `getNodeWithName` | `name` : string <br> | `handle` : handle <br> |
| | Method | `getParamWithName` | `name` : string <br> | `handle` : handle <br> |
| | Method | `getSpatialParametersAtTime` | `time` : double <br> | `double[]` : double[] <br> |
| | Method | `getTimeline` | None | `handle` : handle <br> |
| | Method | `setName` | `name` : string <br> | `null` : null <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `resetLayer` | None | `null` : null <br> |
| | Method | `getLayerJsonDescrip` | None | `string` : string <br> |
| | Method | `setLayerJsonDescrip` | `descrip` : string <br>`makeAllDominant` : bool <br> | `null` : null <br> |
| | Method | `getJsonDescrip` | None | `string` : string <br> |
| | Method | `initFromJsonDescrip` | `descrip` : string <br> | `null` : null <br> |
| | Method | `setOpacity` | `value` : double <br> | `null` : null <br> |
| | Method | `getOpacity` | None | `double` : double <br> |
| | Method | `resetOpacity` | None | `null` : null <br> |
| | Method | `setVolume` | `value` : double <br> | `null` : null <br> |
| | Method | `getVolume` | None | `double` : double <br> |
| | Method | `resetVolume` | None | `null` : null <br> |
| | Method | `muteLayer` | None | `null` : null <br> |
| | Method | `unMuteLayer` | None | `null` : null <br> |
| | Method | `getIsLayerMuted` | None | `bool` : bool <br> |
| | Method | `muteAudio` | None | `null` : null <br> |
| | Method | `unMuteAudio` | None | `null` : null <br> |
| | Method | `getIsAudioMuted` | None | `bool` : bool <br> |
| | Method | `getDmxMuteState` | None | `int` : int <br> |
| | Method | `setDmxMuteState` | `muteState` : uint <br> | `null` : null <br> |
| | Method | `toggleExplicitMute` | `flag` : uint <br> | `null` : null <br> |
| | Method | `setTransport` | `mode` : int <br>`loop` : bool <br> | `null` : null <br> |
| | Method | `getTransportMode` | None | `int` : int <br> |
| | Method | `resetTransportMode` | None | `null` : null <br> |
| | Method | `getTransportLoop` | None | `bool` : bool <br> |
| | Method | `assignResource` | `id` : double <br> | `null` : null <br> |
| | Method | `assignResourceWithFade` | `id` : double <br>`fadeDuration` : double <br> | `null` : null <br> |
| | Method | `getAssignedResource` | None | `handle` : handle <br> |
| | Method | `resetAssignedResource` | None | `null` : null <br> |
| | Method | `getAssignedModelResource` | None | `handle` : handle <br> |
| | Method | `resetAssignedModelResource` | None | `null` : null <br> |
| | Method | `getFxNames` | None | `string[]` : string[] <br> |
| | Method | `setFadeDurationDominantResourceChange` | `value` : double <br> | `null` : null <br> |
| | Method | `getFadeDurationDominantResourceChange` | None | `double` : double <br> |
| | Method | `createClip` | None | `handle` : handle <br> |
| | Method | `createClipAtTime` | `timeInFrames` : double <br> | `handle` : handle <br> |
| | Method | `controlClipBorder` | `clip` : handle <br>`isEnter` : bool <br>`isIncremental` : bool <br>`entryTime` : double <br> | `null` : null <br> |
| | Method | `getClipAtIndex` | `index` : int <br> | `handle` : handle <br> |
| | Method | `getClips` | None | `handle[]` : handle[] <br> |
| | Method | `getClipCurrent` | `offset` : int <br> | `handle` : handle <br> |
| | Method | `getClipsSelected` | None | `handle[]` : handle[] <br> |
| | Method | `removeClips` | None | `null` : null <br> |
| | Method | `setHomeScreenFromScreenName` | `screenName` : string <br> | `null` : null <br> |
| | Method | `getHomeScreenName` | None | `string` : string <br> |
| | Method | `setBlendMode` | `blendMode` : string <br> | `null` : null <br> |
| | Method | `getBlendMode` | None | `string` : string <br> |
| | Method | `addEffectById` | `id` : double <br> | `null` : null <br> |
| | Method | `setPreloadPermanently` | `doPreloadPermanently` : bool <br> | `null` : null <br> |
| | Method | `getPreloadPermanently` | None | `bool` : bool <br> |
| | Method | `setRestrictToServiceWithIps` | `doRestrict` : bool <br>`ipAdresses` : string[] <br> | `null` : null <br> |
| | Method | `getRestrictToService` | None | `bool` : bool <br> |
| | Method | `getRestrictedServiceIps` | None | `string[]` : string[] <br> |
| | Method | `getOffsets` | None | `double[]` : double[] <br> |
| | Method | `setOffsets` | `x` : optional<double> <br>`y` : optional<double> <br>`z` : optional<double> <br>`xr` : optional<double> <br>`yr` : optional<double> <br>`zr` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `null` : null <br> |
| | Method | `setCurrentValuesToOffset` | `typeIndex` : int <br>`resetDominant` : optional<bool> <br>`removeKeyframesClips` : optional<bool> <br> | `null` : null <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `Clip` | | |
| | Method | `getId` | None | `double` : double <br> |
| | Method | `removeThis` | None | `null` : null <br> |
| | Method | `getTimeline` | None | `handle` : handle <br> |
| | Method | `setTime` | `time` : double <br> | `null` : null <br> |
| | Method | `getTime` | None | `double` : double <br> |
| | Method | `setDuration` | `duration` : double <br> | `null` : null <br> |
| | Method | `getDuration` | None | `double` : double <br> |
| | Method | `setLabel` | `label` : string <br> | `null` : null <br> |
| | Method | `getLabel` | None | `string` : string <br> |
| | Method | `getPlayMode` | None | `int` : int <br> |
| | Method | `setPlayMode` | `playMode` : int <br> | `null` : null <br> |
| | Method | `getSpeed` | None | `double` : double <br> |
| | Method | `setSpeed` | `speed` : double <br> | `null` : null <br> |
| | Method | `getBlendFrames` | None | `bool` : bool <br> |
| | Method | `setBlendFrames` | `doFrameblending` : bool <br> | `null` : null <br> |
| | Method | `getInpoint` | None | `double` : double <br> |
| | Method | `setInpoint` | `inpoint` : double <br> | `null` : null <br> |
| | Method | `getOutpoint` | None | `double` : double <br> |
| | Method | `setOutpoint` | `inpoint` : double <br> | `null` : null <br> |
| | Method | `assignResource` | `resId` : double <br>`setToResourceDuration` : optional<bool> <br> | `null` : null <br> |
| | Method | `getAssignedResource` | None | `handle` : handle <br> |
| | Method | `setToResourceDuration` | None | `null` : null <br> |
| | Method | `createEvent` | `namePath` : string <br>`time` : double <br>`value` : double <br> | `null` : null <br> |
| | Method | `createEventInPixelSpace` | `namePath` : string <br>`time` : double <br>`value` : double <br> | `null` : null <br> |
| | Method | `removeEvent` | `namePath` : string <br>`time` : double <br> | `null` : null <br> |
| | Method | `createPauseCueBeforeClip` | None | `handle` : handle <br> |
| | Method | `setColorTransformPath` | `colorTransformPath` : string <br> | `null` : null <br> |
| | Method | `getColorTransformPath` | None | `string` : string <br> |
| | Method | `clearColorTransformPath` | None | `null` : null <br> |
| | Method | `getKeyframesAsJsonString` | None | `string` : string <br> |
| Class | | `Node` | | |
| | Method | `getParameters` | None | `handle[]` : handle[] <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `getParamWithName` | `name` : string <br> | `handle` : handle <br> |
| | Method | `setValues` | `values` : double[] <br> | `null` : null <br> |
| | Method | `getValues` | None | `double[]` : double[] <br> |
| | Method | `resetValues` | None | `null` : null <br> |
| | Method | `storeValues` | None | `null` : null <br> |
| | Method | `mute` | None | `null` : null <br> |
| | Method | `unMute` | None | `null` : null <br> |
| | Method | `getIsMuted` | None | `bool` : bool <br> |
| | Method | `getTimeline` | None | `handle` : handle <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `Param` | | |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `getIsChannel` | None | `bool` : bool <br> |
| | Method | `setValue` | `value` : timelineParamValue <br> | `null` : null <br> |
| | Method | `setValueRelativ` | `value` : double <br> | `null` : null <br> |
| | Method | `getValue` | None | `timelineParamValue` : timelineParamValue <br> |
| | Method | `resetValue` | None | `null` : null <br> |
| | Method | `storeValue` | None | `null` : null <br> |
| | Method | `setTransportAttributes` | `mode` : int <br>`speed` : double <br>`loop` : bool <br>`inpoint` : int <br>`outpoint` : int <br> | `null` : null <br> |
| | Method | `getAttributes` | None | `TransportAttributes` : TransportAttributes <br> |
| | Method | `mute` | None | `null` : null <br> |
| | Method | `unMute` | None | `null` : null <br> |
| | Method | `getIsMuted` | None | `bool` : bool <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |
| Class | | `Cue` | | |
| | Method | `removeThis` | None | `null` : null <br> |
| | Method | `apply` | None | `null` : null <br> |
| | Method | `blendToThis` | `blendDurationInSeconds` : double <br> | `null` : null <br> |
| | Method | `getAttributes` | None | `CueAttributes` : CueAttributes <br> |
| | Method | `getTimeline` | None | `handle` : handle <br> |
| | Method | `getIndex` | None | `int` : int <br> |
| | Method | `getName` | None | `string` : string <br> |
| | Method | `setName` | `name` : string <br> | `bool` : bool <br> |
| | Method | `getNote` | None | `string` : string <br> |
| | Method | `setNote` | `note` : string <br> | `bool` : bool <br> |
| | Method | `getOperation` | None | `int` : int <br> |
| | Method | `setOperation` | `operation` : int <br> | `bool` : bool <br> |
| | Method | `getJumpMode` | None | `int` : int <br> |
| | Method | `setJumpMode` | `jumpMode` : int <br> | `bool` : bool <br> |
| | Method | `getJumpGoalTime` | None | `double` : double <br> |
| | Method | `setJumpGoalTime` | `time` : double <br> | `bool` : bool <br> |
| | Method | `getJumpGoalLabel` | None | `string` : string <br> |
| | Method | `getJumpGoalCue` | None | `handle` : handle <br> |
| | Method | `setJumpGoalLabel` | `jumpGoalLabel` : string <br> | `bool` : bool <br> |
| | Method | `getNumber` | None | `int` : int <br> |
| | Method | `setNumber` | `number` : int <br> | `null` : null <br> |
| | Method | `getWaitDuration` | None | `double` : double <br> |
| | Method | `setWaitDuration` | `time` : double <br> | `bool` : bool <br> |
| | Method | `getBlendDuration` | None | `double` : double <br> |
| | Method | `setBlendDuration` | `timeInFrames` : double <br> | `bool` : bool <br> |
| | Method | `getTime` | None | `double` : double <br> |
| | Method | `setTime` | `time` : double <br> | `bool` : bool <br> |
| | Method | `getTimelineToTriggerName` | None | `string` : string <br> |
| | Method | `setTimelineToTrigger` | `nameTimeline` : string <br> | `bool` : bool <br> |
| | Method | `getTimelineTriggerMode` | None | `int` : int <br> |
| | Method | `setTimelineTriggerMode` | `mode` : int <br> | `bool` : bool <br> |
| | Method | `getTimelineTriggerApplyTime` | None | `double` : double <br> |
| | Method | `setTimelineTriggerApplyTime` | `time` : double <br> | `bool` : bool <br> |
| | Method | `setTimelineTriggerApplyCue` | `goalCueLabel` : string <br> | `bool` : bool <br> |
| | Method | `getCountdown` | None | `double` : double <br> |
| | Method | `getCountdownHMSF` | None | `string` : string <br> |
| | Method | `setCommand` | `conveyorName` : string <br>`commandData` : string <br> | `null` : null <br> |
| | Method | `getInst` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getHandleFromInstancePath` | `instancePath` : string <br> | `handle` : handle <br> |
| | Method | `getInstancePath` | None | `string` : string <br> |

## Calibration
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `setMarkerPositions` | `positions` : double[] <br>`markerIds` : int[] <br> | `null` : null <br> |

## WebViews
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `loadDeviceUi` | `devicePath` : string <br> | `null` : null <br> |
| Function | | `activatePreviousFunc` | None | `null` : null <br> |
| Function | | `activateNextFunc` | None | `null` : null <br> |
| Function | | `getLastActivatedFunc` | None | `string` : string <br> |
| Function | | `deviceActivated` | `devicePath` : string <br>`withSelection` : bool <br> | `null` : null <br> |
| Function | | `funcActivated` | `funcPath` : string <br>`withSelection` : bool <br> | `null` : null <br> |
| Function | | `setFuncBodyState` | `funcPath` : string <br>`state` : string <br> | `null` : null <br> |
| Function | | `getFuncBodyState` | `funcPath` : string <br> | `string` : string <br> |
| Function | | `setTag` | `tag` : string <br>`text` : string <br> | `null` : null <br> |
| Function | | `setEditorIsUsingBlocks` | `useBlocks` : bool <br> | `null` : null <br> |

## Ui
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `getComboBoxWithId` | `id` : double <br> | `handle` : handle <br> |
| Function | | `setAppMode` | `mode` : int <br> | `null` : null <br> |
| Function | | `getAppMode` | None | `int` : int <br> |
| Function | | `getDisplayTestpattern` | None | `bool` : bool <br> |
| Function | | `setDisplayTestpattern` | `display` : bool <br> | `null` : null <br> |
| Function | | `getPreviewCameraAsJsonString` | None | `string` : string <br> |
| Function | | `setPreviewCameraAsJsonString` | `cameraFrustrumStateString` : string <br> | `null` : null <br> |
| Function | | `setDisableContentRendering` | `state` : bool <br> | `null` : null <br> |
| Function | | `getIsContentRenderingDisabled` | None | `bool` : bool <br> |
| Function | | `setDisableWorkspaceRendering` | `state` : bool <br> | `null` : null <br> |
| Function | | `getIsWorkspaceRenderingDisabled` | None | `bool` : bool <br> |
| Class | | `ComboBox` | | |
| | Method | `clear` | None | `null` : null <br> |
| | Method | `addItem` | `item` : string <br>`id` : int <br> | `null` : null <br> |
| | Method | `setSelectedId` | `id` : int <br> | `null` : null <br> |
| | Method | `getSelectedId` | None | `int` : int <br> |

## Direct
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |
| Function | | `setRegistered` | `hdls` : handle[] <br>`expectedFrequency` : int <br>`dampingMs` : int <br>`usageHints` : string[] <br> | `null` : null <br> |
| Function | | `reloadRegistered` | None | `null` : null <br> |
| Function | | `registerScreen` | `name` : string <br>`expectedFrequency` : int <br>`dampingMs` : int <br> | `handle` : handle <br> |
| Function | | `registerParam` | `instancePath` : string <br> | `handle` : handle <br> |
| Function | | `registerCamera` | `cameraName` : string <br>`expectedFrequency` : int <br> | `handle` : handle <br> |
| Function | | `registerPerspective` | `screenName` : string <br>`expectedFrequency` : int <br> | `handle` : handle <br> |
| Class | | `Screen` | | |
| | Method | `setPosition` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br> | `null` : null <br> |
| | Method | `setRotation` | `xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null` : null <br> |
| | Method | `setPosRot` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br> | `null` : null <br> |
| | Method | `setPosRotScale` | `xPos` : optional<double> <br>`yPos` : optional<double> <br>`zPos` : optional<double> <br>`xRot` : optional<double> <br>`yRot` : optional<double> <br>`zRot` : optional<double> <br>`xScale` : optional<double> <br>`yScale` : optional<double> <br>`zScale` : optional<double> <br> | `null` : null <br> |
| | Method | `enableLogging` | `enable` : bool <br> | `null` : null <br> |
| Class | | `Param` | | |
| | Method | `setValue` | `value` : double <br> | `null` : null <br> |
| | Method | `enableLogging` | `enable` : bool <br> | `null` : null <br> |
| Class | | `Camera` | | |
| | Method | `setPosition` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br> | `null` : null <br> |
| | Method | `setRotation` | `xRot` : double <br>`yRot` : double <br>`zRot` : double <br> | `null` : null <br> |
| | Method | `setTransformation` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br> | `null` : null <br> |
| | Method | `setTransformationAndLensProps` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null` : null <br> |
| | Method | `setTransformationAndLensPropsExt` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`focalDistance` : double <br>`zoom` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`k3` : double <br>`p1` : double <br>`p2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br>`overscan` : double <br> | `null` : null <br> |
| Class | | `Perspective` | | |
| | Method | `setTransformation` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br> | `null` : null <br> |
| | Method | `setTransformationAndLensProps` | `xPos` : double <br>`yPos` : double <br>`zPos` : double <br>`xRot` : double <br>`yRot` : double <br>`zRot` : double <br>`fov` : double <br>`aspectRatio` : double <br>`nearClip` : double <br>`farClip` : double <br>`aperture` : double <br>`focus` : double <br>`iris` : double <br>`k1` : double <br>`k2` : double <br>`centerX` : double <br>`centerY` : double <br>`panelWidth` : double <br> | `null` : null <br> |

## Unreal
| Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- |

