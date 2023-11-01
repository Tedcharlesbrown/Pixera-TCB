# API Overview

| Namespace | Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- | --- |
| Utility | Function | | `getApiRevision` | None | `int`: int |
| Utility | Function | | `getHasFunction` | `functionName`: string | `bool`: bool |
| Utility | Function | | `outputDebug` | `message`: string | `string`: string |
| Utility | Function | | `getLicenseJson` | None | `string`: string |
| Utility | Function | | `getCurrentTime` | None | `double`: double |
| Utility | Function | | `getCurrentTimeAsString` | None | `string`: string |
| Utility | Function | | `noop` | None | `null`: null |
| Utility | Function | | `requestCallback` | `functionName`: string | `null`: null |
| Utility | Function | | `readFileString` | `path`: string | `string`: string |
| Utility | Function | | `writeFileString` | `path`: string, `fileStr`: string | `null`: null |
| Utility | Function | | `getAccessRecipe` | `hdlPath`: string | `string`: string |
| Utility | Function | | `pollMonitoring` | None | `string`: string |
| Utility | Function | | `unsubscribeMonitoringSubject` | `subject`: string | `bool`: bool |
| Utility | Function | | `subscribeMonitoringSubject` | `subject`: string | `bool`: bool |
| Utility | Function | | `setMonitoringEventMode` | `mode`: string | `bool`: bool |
| Utility | Function | | `monitoringEvent` | `eventDescription`: string | `null`: null |
| Utility | Function | | `setShowContextInReplies` | `doShow`: bool | `bool`: bool |
| Utility | Function | | `setMonitoringHasDelimiter` | `hasDelimiter`: bool | `bool`: bool |
| Utility | Function | | `runJsScript` | `jsFunction`: string, `jsCode`: string | `string`: string |
| Utility | Function | | `dynamicRebuildFromJsonDescription` | `deviceName`: string, `jsonDescription`: string, `folder`: string | `null`: null |
| Network | Function | | `getConveyor` | `conveyorName`: string | `handle`: handle |
| Network | Class | | `Conveyor` | | |
| | | Method | `sendString` | `str`: string | `null`: null |
| Compound | Function | | `setTransportModeOnTimelineAtIndex` | `index`: int, `mode`: int | `bool`: bool |
| Compound | Function | | `setTransportModeOnTimeline` | `timelineName`: string, `mode`: int | `null`: null |
| Compound | Function | | `toggleTransport` | `timelineName`: string | `null`: null |
| Compound | Function | | `getTransportModeOnTimeline` | `timelineName`: string | `int`: int |
| Compound | Function | | `setOpacityOnTimeline` | `timelineName`: string, `opacity`: double | `null`: null |
| Compound | Function | | `getOpacityOnTimeline` | `timelineName`: string | `double`: double |
| Compound | Function | | `startFirstTimeline` | None | `null`: null |
| Compound | Function | | `pauseFirstTimeline` | None | `null`: null |
| Compound | Function | | `stopFirstTimeline` | None | `null`: null |
| Compound | Function | | `setPosValue` | `val`: double | `null`: null |
| Compound | Function | | `setPosValueXY` | `valX`: double, `valY`: double | `null`: null |
| Compound | Function | | `setParamValue` | `path`: string, `value`: double | `null`: null |
| Compound | Function | | `applyCueAtIndexOnTimelineAtIndex` | `cueIndex`: int, `timelineIndex`: int | `null`: null |
| Compound | Function | | `applyCueNumberOnTimelineAtIndex` | `cueNumber`: int, `timelineIndex`: int | `null`: null |
| Compound | Function | | `applyCueNumberOnTimeline` | `timelineName`: string, `cueNumber`: int | `null`: null |
| Compound | Function | | `applyCueOnTimeline` | `timelineName`: string, `cueName`: string | `null`: null |
| Compound | Function | | `addResourceToFolder` | `namePath`: string, `filePath`: string | `handle`: handle |
| Compound | Function | | `assignResourceToLayer` | `resourcePath`: string, `layerPath`: string | `null`: null |
| Compound | Function | | `refreshResource` | `resourcePath`: string | `null`: null |
| Compound | Function | | `setTransportModeOnLayer` | `layerPath`: string, `mode`: int, `loop`: bool | `null`: null |
| Compound | Function | | `getTransportModeOnLayer` | `layerPath`: string | `int`: int |
| Compound | Function | | `getResourceAssignedToLayer` | `layerPath`: string | `string`: string |
| Compound | Function | | `assignResourceToClipAtTimeByDmxId` | `layerPath`: string, `dmxFolderId`: int, `dmxFileId`: int, `time`: double | `null`: null |
| Compound | Function | | `assignResourceToClipAtHMSFStringByDmxId` | `layerPath`: string, `dmxFolderId`: int, `dmxFileId`: int, `hmsf`: string | `null`: null |
| Compound | Function | | `assignResourceToClipAtHMSFByDmxId` | `layerPath`: string, `dmxFolderId`: int, `dmxFileId`: int, `h`: int, `m`: int, `s`: int, `f`: int | `null`: null |
| Compound | Function | | `setCurrentTimeOfTimeline` | `timelineName`: string, `time`: int | `null`: null |
| Compound | Function | | `setCurrentTimeOfTimelineInSeconds` | `timelineName`: string, `time`: double | `null`: null |
| Compound | Function | | `setCurrentTimeAndTransportModeOfTimelineInSeconds` | `timelineName`: string, `time`: double, `mode`: int | `null`: null |
| Compound | Function | | `getFpsOfTimeline` | `timelineName`: string | `double`: double |
| Compound | Function | | `getCurrentTimeOfTimeline` | `timelineName`: string | `int`: int |
| Compound | Function | | `getCurrentTimeOfTimelineInSeconds` | `timelineName`: string | `double`: double |
| Compound | Function | | `getCurrentHMSFOfTimeline` | `timelineName`: string | `string`: string |
| Compound | Function | | `getCurrentCountdownOfTimeline` | `timelineName`: string | `int`: int |
| Compound | Function | | `getCurrentCountdownHMSFOfTimeline` | `timelineName`: string | `string`: string |
| Compound | Function | | `startOpacityAnimationOfTimeline` | `timelineName`: string, `fadeIn`: bool, `fullFadeDuration`: double | `null`: null |
| Compound | Function | | `createClipOnLayerAtTimeWithResource` | `layerPath`: string, `time`: double, `resourcePath`: string | `null`: null |
| Compound | Function | | `removeClipOnLayerWithIndex` | `layerPath`: string, `clipIndex`: int | `null`: null |
| Compound | Function | | `removeAllClipsOnLayer` | `layerPath`: string | `null`: null |
| Compound | Function | | `getClipDurationInSecondsWithIndex` | `layerPath`: string, `clipIndex`: int | `double`: double |
| Compound | Function | | `getClipDurationInFramesWithIndex` | `layerPath`: string, `clipIndex`: int | `int`: int |
| Compound | Function | | `getClipTimeInSecondsWithIndex` | `layerPath`: string, `clipIndex`: int | `double`: double |
| Compound | Function | | `getClipEndTimeInSecondsWithIndex` | `layerPath`: string, `clipIndex`: int | `double`: double |
| Compound | Function | | `getResourceDurationInSeconds` | `resourcePath`: string | `double`: double |
| Compound | Function | | `getParamValue` | `path`: string | `double`: double |
| Compound | Function | | `setTimecodeInput` | `hour`: int, `minute`: int, `second`: int, `frame`: int, `elapsedTime`: double, `running`: bool, `freshMode`: int, `stateToken`: int, `format`: int | `double`: double |
| Compound | Function | | `takeOverAllClients` | None | `null`: null |
| Compound | Function | | `setPauseSmpteInput` | `doPause`: bool | `null`: null |
| Session | Function | | `closeApp` | `saveProject`: bool | `null`: null |
| Session | Function | | `loadProject` | `path`: string | `null`: null |
| Session | Function | | `saveProject` | None | `null`: null |
| Session | Function | | `saveProjectAs` | `path`: string | `null`: null |
| Session | Function | | `getProjectName` | None | `string`: string |
| Session | Function | | `setProjectName` | `name`: string | `null`: null |
| Session | Function | | `getProjectDirectory` | None | `string`: string |
| Session | Function | | `getControlMultiUserSessionName` | None | `string`: string |
| Session | Function | | `shutdownSystem` | `mode`: optional<int> | `null`: null |
| Session | Function | | `getLiveSystemIps` | None | `string[]`: string[] |
| Session | Function | | `getLiveSystemState` | `ip`: string | `string`: string |
| Session | Function | | `liveSystemStateChange` | `ip`: string, `state`: string | `null`: null |
| Session | Function | | `shutdownLiveSystem` | `ip`: string, `mode`: optional<int> | `null`: null |
| Session | Function | | `wakeLiveSystem` | `ip`: string | `string`: string |
| Session | Function | | `getLiveSystemMacAddress` | `ip`: string | `string`: string |
| Session | Function | | `startLiveSystem` | `ip`: string | `null`: null |
| Session | Function | | `startLiveSystems` | None | `null`: null |
| Session | Function | | `stopLiveSystem` | `ip`: string | `null`: null |
| Session | Function | | `stopLiveSystems` | None | `null`: null |
| Session | Function | | `restartLiveSystem` | `ip`: string | `null`: null |
| Session | Function | | `restartLiveSystems` | None | `null`: null |
| Session | Function | | `remoteSystemStateChange` | `ip`: string, `state`: string | `null`: null |
| Session | Function | | `getRemoteSystemIps` | None | `string[]`: string[] |
| Session | Function | | `getRemoteSystemState` | `ip`: string | `string`: string |
| Session | Function | | `setVideoStreamActiveState` | `ip`: string, `device`: string, `isActive`: bool | `null`: null |
| Session | Function | | `getVideoStreamActiveState` | `ip`: string, `device`: string | `bool`: bool |
| Session | Function | | `getDefaultClipDurationsAsJsonString` | None | `string`: string |
| LiveSystems | Function | | `getLiveSystems` | None | `handle[]`: handle[] |
| LiveSystems | Function | | `liveSystemNotAvailable` | `reason`: int, `system`: handle | `null`: null |
| LiveSystems | Function | | `getMultiUserMembers` | None | `handle[]`: handle[] |
| LiveSystems | Class | | `MultiUserMember` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `getIp` | None | `string`: string |
| | | Method | `getState` | None | `string`: string |
| | | Method | `getPerformanceMonitoringValuesJson` | None | `string`: string |
| | | Method | `getPerformanceMonitoringValuesJsonEx` | `filter`: string | `string`: string |
| | | Method | `resetCumulativePerformanceMonitoringValues` | None | `null`: null |
| | | Method | `ensureFileDistribution` | `includeNotUsedYet`: bool | `null`: null |
| | | Method | `shutDown` | `mode`: int | `null`: null |
| | | Method | `wakeUp` | None | `string`: string |
| | | Method | `getMacAddress` | None | `string`: string |
| | | Method | `resetEngine` | None | `null`: null |
| | | Method | `restartEngine` | None | `null`: null |
| | | Method | `startEngine` | None | `null`: null |
| | | Method | `closeEngine` | None | `null`: null |
| | | Method | `triggerBackup` | `applyControlCommand`: optional<bool> | `null`: null |
| | | Method | `getStructureJson` | None | `string`: string |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| LiveSystems | Class | | `LiveSystem` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `getIp` | None | `string`: string |
| | | Method | `getState` | None | `string`: string |
| | | Method | `setBackupRole` | `role`: int | `null`: null |
| | | Method | `getBackupRole` | None | `int`: int |
| | | Method | `getPerformanceMonitoringValuesJson` | None | `string`: string |
| | | Method | `getPerformanceMonitoringValuesJsonEx` | `filter`: string | `string`: string |
| | | Method | `resetCumulativePerformanceMonitoringValues` | None | `null`: null |
| | | Method | `moveMappingsToOutputs` | `hdlSrc`: handle, `outputIdPathMapStr`: string | `null`: null |
| | | Method | `clearExportedMappings` | `path`: string, `onlyServicePath`: bool | `null`: null |
| | | Method | `exportMappings` | `path`: string | `null`: null |
| | | Method | `importMappings` | `path`: string, `outputIdPathMapStr`: string | `null`: null |
| | | Method | `exportMappingsDirectly` | `path`: string | `null`: null |
| | | Method | `importMappingsDirectly` | `path`: string, `outputIdPathMapStr`: string | `null`: null |
| | | Method | `exportMappingsToLiveSystemPath` | `parentPath`: string | `null`: null |
| | | Method | `importMappingsFromLiveSystemPath` | `parentPath`: string | `null`: null |
| | | Method | `clearExportedMappingsAtLiveSystemPath` | `path`: string | `null`: null |
| | | Method | `ensureFileDistribution` | `includeNotUsedYet`: bool | `null`: null |
| | | Method | `shutDown` | `mode`: int | `null`: null |
| | | Method | `wakeUp` | None | `string`: string |
| | | Method | `getMacAddress` | None | `string`: string |
| | | Method | `getGraphicsDevices` | None | `handle[]`: handle[] |
| | | Method | `getEnabledOutputs` | None | `handle[]`: handle[] |
| | | Method | `getAllOutputs` | None | `handle[]`: handle[] |
| | | Method | `getVideoStreamOutputs` | None | `handle[]`: handle[] |
| | | Method | `resetEngine` | None | `null`: null |
| | | Method | `restartEngine` | None | `null`: null |
| | | Method | `startEngine` | None | `null`: null |
| | | Method | `closeEngine` | None | `null`: null |
| | | Method | `setAudioMasterVolume` | `channel`: int, `volume`: double | `null`: null |
| | | Method | `getAudioMasterVolume` | `channel`: int | `double`: double |
| | | Method | `setAudioMasterMute` | `channel`: int, `state`: bool | `null`: null |
| | | Method | `getAudioMasterMute` | `channel`: int | `bool`: bool |
| | | Method | `setAudioTimecodeInput` | `channel`: int, `state`: bool | `null`: null |
| | | Method | `triggerBackup` | `applyControlCommand`: optional<bool> | `null`: null |
| | | Method | `getStructureJson` | None | `string`: string |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| LiveSystems | Class | | `GraphicsDevice` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `getEnabledOutputs` | None | `handle[]`: handle[] |
| | | Method | `getAllOutputs` | None | `handle[]`: handle[] |
| LiveSystems | Class | | `Output` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setActive` | `active`: bool | `null`: null |
| | | Method | `getActive` | None | `bool`: bool |
| | | Method | `setIdentify` | `state`: bool | `null`: null |
| | | Method | `getIdentify` | None | `bool`: bool |
| | | Method | `getAssignedScreens` | None | `handle[]`: handle[] |
| | | Method | `getAssignedProjectors` | None | `handle[]`: handle[] |
| | | Method | `getEnabled` | None | `bool`: bool |
| | | Method | `getForPreview` | None | `bool`: bool |
| LiveSystems | Class | | `VideoStream` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setActive` | `active`: bool | `null`: null |
| | | Method | `getActive` | None | `bool`: bool |
| Screens | Function | | `getScreenWithName` | `name`: string | `handle`: handle |
| Screens | Function | | `setNamedScreenPosition` | `name`: string, `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `null`: null |
| Screens | Function | | `getScreens` | None | `handle[]`: handle[] |
| Screens | Function | | `getScreenNames` | None | `string[]`: string[] |
| Screens | Function | | `getFirstTimelineWithHomeScreen` | `screenName`: string | `handle`: handle |
| Screens | Function | | `getStudioCameras` | None | `handle[]`: handle[] |
| Screens | Class | | `Screen` | | |
| | | Method | `getId` | None | `double`: double |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `bool`: bool |
| | | Method | `getPosition` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `bool`: bool |
| | | Method | `getRotation` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setScale` | `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | `bool`: bool |
| | | Method | `getScale` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setPosRot` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `bool`: bool |
| | | Method | `setPosRotScale` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | `bool`: bool |
| | | Method | `getPersepective` | None | `handle`: handle |
| | | Method | `snapPerspectiveCornersToScreen` | `mode`: int | `null`: null |
| | | Method | `setPerspectivePosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `bool`: bool |
| | | Method | `setPerspectivePositionWithLookAt` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `bool`: bool |
| | | Method | `getPerspectivePosition` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setPerspectiveRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `bool`: bool |
| | | Method | `getPerspectiveRotation` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setCameraPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `bool`: bool |
| | | Method | `setCameraPositionWithLookAt` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `bool`: bool |
| | | Method | `getCameraPosition` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setCameraRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `bool`: bool |
| | | Method | `getCameraRotation` | None | `ScreenPosValues`: ScreenPosValues |
| | | Method | `setContentSamplingFrustumBase` | `x`: double, `y`: double, `width`: double, `height`: double, `rotation`: double, `originScreenId`: double | `null`: null |
| | | Method | `runCalibration` | `mode`: string, `diff`: string | `null`: null |
| | | Method | `editCalibration` | `diff`: string | `null`: null |
| | | Method | `resetWarpFile` | `diff`: string | `null`: null |
| | | Method | `loadWarpFile` | `filePath`: string | `null`: null |
| | | Method | `loadWarpFileWithDiff` | `filePath`: string, `diff`: string | `null`: null |
| | | Method | `addWarpFile` | `filePath`: string | `null`: null |
| | | Method | `addWarpFileWithDiff` | `filePath`: string, `diff`: string | `null`: null |
| | | Method | `loadColorCalibration` | `calibrationName`: string | `null`: null |
| | | Method | `runColorCalibration` | None | `null`: null |
| | | Method | `setIsVisible` | `isVisible`: bool | `null`: null |
| | | Method | `getIsVisible` | None | `bool`: bool |
| | | Method | `setIsProjectable` | `isProjectable`: bool | `null`: null |
| | | Method | `getIsProjectable` | None | `bool`: bool |
| | | Method | `triggerRefreshMapping` | None | `null`: null |
| | | Method | `resetAllColorCorrections` | None | `null`: null |
| | | Method | `setColorCorrectionWithPath` | `path`: string, `value`: float | `null`: null |
| | | Method | `getColorCorrectionWithPath` | `path`: string | `float`: float |
| | | Method | `setColorCorrectionAsJsonString` | `colorCorrection`: string | `null`: null |
| | | Method | `getColorCorrectionAsJsonString` | None | `string`: string |
| | | Method | `getOutput` | None | `handle[]`: handle[] |
| | | Method | `setBlackout` | `isActive`: bool | `null`: null |
| | | Method | `getBlackout` | None | `bool`: bool |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Screens | Class | | `StudioCamera` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `null`: null |
| | | Method | `getPosition` | `xPos`: double, `yPos`: double, `zPos`: double | `double[]`: double[] |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `null`: null |
| | | Method | `getRotation` | `xPos`: double, `yPos`: double, `zPos`: double | `double[]`: double[] |
| | | Method | `setTransformation` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `fov`: optional<double>, `aspectRatio`: optional<double> | `null`: null |
| | | Method | `setTransformationAndLensProps` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `iris`: double, `k1`: double, `k2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double | `null`: null |
| | | Method | `setTransformationAndLensPropsExt` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `focalDistance`: double, `zoom`: double, `iris`: double, `k1`: double, `k2`: double, `k3`: double, `p1`: double, `p2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double, `overscan`: double | `null`: null |
| | | Method | `setTrackingInputPause` | `pause`: bool | `null`: null |
| | | Method | `getTrackingInputPause` | None | `bool`: bool |
| | | Method | `setUsePositionPropertiesFromTracking` | `pause`: bool | `null`: null |
| | | Method | `getUsePositionPropertiesFromTracking` | None | `bool`: bool |
| | | Method | `setUseRotationPropertiesFromTracking` | `pause`: bool | `null`: null |
| | | Method | `getUseRotationPropertiesFromTracking` | None | `bool`: bool |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Screens | Class | | `Perspective` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setTransformation` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `fov`: optional<double>, `aspectRatio`: optional<double> | `null`: null |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Projectors | Function | | `getProjectorWithName` | `name`: string | `handle`: handle |
| Projectors | Function | | `getProjectors` | None | `handle[]`: handle[] |
| Projectors | Function | | `getProjectorNames` | None | `string[]`: string[] |
| Projectors | Class | | `Projector` | | |
| | | Method | `getPosition` | None | `ProjectorPosValues`: ProjectorPosValues |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `bool`: bool |
| | | Method | `getRotation` | None | `ProjectorPosValues`: ProjectorPosValues |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `bool`: bool |
| | | Method | `getName` | None | `string`: string |
| | | Method | `activateScreenMapping` | `screenId`: double, `isActive`: bool | `null`: null |
| | | Method | `setBlackout` | `isActive`: bool | `null`: null |
| | | Method | `getBlackout` | None | `bool`: bool |
| | | Method | `setSoftedgeVisible` | `screenName`: string, `visible`: bool | `null`: null |
| | | Method | `resetAllColorCorrections` | None | `null`: null |
| | | Method | `setColorCorrectionWithPath` | `path`: string, `value`: float | `null`: null |
| | | Method | `getColorCorrectionWithPath` | `path`: string | `float`: float |
| | | Method | `setColorCorrectionAsJsonString` | `colorCorrection`: string | `null`: null |
| | | Method | `getColorCorrectionAsJsonString` | None | `string`: string |
| | | Method | `getOutput` | None | `handle`: handle |
| | | Method | `setOutput` | `outputHandle`: handle | `null`: null |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Resources | Function | | `getResources` | None | `handle[]`: handle[] |
| Resources | Function | | `getResourceFolderWithNamePath` | `namePath`: string | `handle`: handle |
| Resources | Function | | `getResourceFolders` | None | `handle[]`: handle[] |
| Resources | Function | | `getTranscodingFolders` | None | `handle[]`: handle[] |
| Resources | Function | | `getJsonDescrip` | None | `string`: string |
| Resources | Class | | `ResourceFolder` | | |
| | | Method | `ref` | None | `handle`: handle |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setName` | `name`: string | `null`: null |
| | | Method | `getResourceFolders` | None | `handle[]`: handle[] |
| | | Method | `getResources` | None | `handle[]`: handle[] |
| | | Method | `getResourceAtIndex` | `index`: int | `handle`: handle |
| | | Method | `addResource` | `path`: string | `handle`: handle |
| | | Method | `addResourcesFromDirectory` | `path`: string, `removeOthers`: bool, `checkRedundancy`: bool | `handle[]`: handle[] |
| | | Method | `addResourcesFromDirectoryRemoveAssets` | `path`: string, `removeOthers`: bool, `checkRedundancy`: bool | `handle[]`: handle[] |
| | | Method | `addInternalResource` | `signature`: string, `resKind`: int | `handle`: handle |
| | | Method | `createFoldersFrom` | `path`: string | `null`: null |
| | | Method | `refreshResources` | None | `null`: null |
| | | Method | `moveResourceToThis` | `id`: double | `null`: null |
| | | Method | `removeThis` | None | `null`: null |
| | | Method | `removeThisIncludingAssets` | None | `null`: null |
| | | Method | `removeAllContents` | None | `null`: null |
| | | Method | `removeAllContentsIncludingAssets` | None | `null`: null |
| | | Method | `deleteAllContentsAssetsFromLiveSystem` | `apEntityLiveSystemHandle`: handle | `null`: null |
| | | Method | `resetDistributionTargets` | None | `null`: null |
| | | Method | `changeDistributionTarget` | `apEntityLiveSystemHandle`: handle, `shouldDistribute`: bool | `null`: null |
| | | Method | `replaceResourcesByString` | `searchString`: string, `replaceString`: string, `path`: string | `null`: null |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| | | Method | `getDmxId` | None | `int`: int |
| | | Method | `getCombinedDmxId` | None | `int`: int |
| | | Method | `setDmxId` | `id`: int | `null`: null |
| Resources | Class | | `TranscodingFolder` | | |
| | | Method | `getUsedTranscodingPreset` | None | `string`: string |
| | | Method | `setUsedTranscodingPreset` | `preset`: string | `null`: null |
| | | Method | `getTranscodeAutomatically` | None | `bool`: bool |
| | | Method | `setTranscodeAutomatically` | `autoTranscode`: bool | `null`: null |
| | | Method | `getUseRxCacheAsDestination` | None | `bool`: bool |
| | | Method | `setRxCacheAsDestination` | `useRxCache`: bool | `null`: null |
| | | Method | `getDestinationDirectory` | None | `string`: string |
| | | Method | `setDestinationDirectory` | `path`: string | `null`: null |
| Resources | Class | | `Resource` | | |
| | | Method | `ref` | None | `handle`: handle |
| | | Method | `removeThis` | None | `null`: null |
| | | Method | `deleteFilesOnSystems` | None | `null`: null |
| | | Method | `removeThisIncludingAssets` | None | `null`: null |
| | | Method | `deleteAssetFromLiveSystem` | `apEntityLiveSystemHandle`: handle | `null`: null |
| | | Method | `resetDistributionTargets` | None | `null`: null |
| | | Method | `changeDistributionTarget` | `apEntityLiveSystemHandle`: handle, `shouldDistribute`: bool | `null`: null |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setName` | `name`: string | `null`: null |
| | | Method | `getFps` | None | `double`: double |
| | | Method | `getResolution` | None | `double[]`: double[] |
| | | Method | `getIsActive` | None | `bool`: bool |
| | | Method | `getVideoStreamModes` | None | `string[]`: string[] |
| | | Method | `setVideoStreamMode` | `index`: int | `null`: null |
| | | Method | `getId` | None | `double`: double |
| | | Method | `getDuration` | None | `double`: double |
| | | Method | `getType` | None | `string`: string |
| | | Method | `setCurrentVersion` | `version`: string | `null`: null |
| | | Method | `getCurrentVersion` | None | `string`: string |
| | | Method | `getVersions` | None | `string[]`: string[] |
| | | Method | `getVersionSuffix` | None | `string[]`: string[] |
| | | Method | `rescanVersions` | None | `null`: null |
| | | Method | `getThumbnailAsBase64` | None | `string`: string |
| | | Method | `getHasPendingTransfer` | None | `bool`: bool |
| | | Method | `getIsInUse` | None | `double`: double |
| | | Method | `getLastUsageBeginTime` | None | `double`: double |
| | | Method | `getLastUsageBeginTimeAsString` | None | `string`: string |
| | | Method | `getLastUsageEndTime` | None | `double`: double |
| | | Method | `getLastUsageEndTimeAsString` | None | `string`: string |
| | | Method | `getFilePath` | None | `string`: string |
| | | Method | `setText` | `text`: string | `null`: null |
| | | Method | `getText` | None | `string`: string |
| | | Method | `setFontWithName` | `fontName`: string | `bool`: bool |
| | | Method | `getFontName` | None | `string`: string |
| | | Method | `setFontWithPath` | `fontPath`: string | `bool`: bool |
| | | Method | `setHorizontalTextAlignment` | `textAlignment`: int | `bool`: bool |
| | | Method | `getHorizontalTextAlignment` | None | `int`: int |
| | | Method | `setVerticalTextAlignment` | `textAlignment`: int | `bool`: bool |
| | | Method | `getVerticalTextAlignment` | None | `int`: int |
| | | Method | `setLineHeight` | `lineHeight`: double | `bool`: bool |
| | | Method | `getLineHeight` | None | `double`: double |
| | | Method | `getTextMeasurementsWidthAndHeight` | None | `int[]`: int[] |
| | | Method | `setUrl` | `url`: string | `null`: null |
| | | Method | `getUrl` | None | `string`: string |
| | | Method | `setColorTransformPath` | `colorTransformPath`: string | `null`: null |
| | | Method | `getColorTransformPath` | None | `string`: string |
| | | Method | `clearColorTransformPath` | None | `null`: null |
| | | Method | `refresh` | `text`: string | `null`: null |
| | | Method | `distribute` | None | `null`: null |
| | | Method | `getDmxId` | None | `int`: int |
| | | Method | `setDmxId` | `id`: int | `null`: null |
| | | Method | `removeMultiresourceIndex` | `index`: int | `null`: null |
| | | Method | `addMultiresourceItem` | `id`: double | `null`: null |
| | | Method | `getMultiresourceItems` | None | `handle[]`: handle[] |
| | | Method | `replaceMultiresourceItemByIndex` | `index`: int, `id`: double | `null`: null |
| | | Method | `setMultiresourceResolution` | `width`: int, `height`: int | `null`: null |
| | | Method | `setMultiresourceItemSizebyIndex` | `index`: int, `width`: double, `height`: double | `null`: null |
| | | Method | `setMultiresourceItemPositionbyIndex` | `index`: int, `x`: double, `y`: double | `null`: null |
| | | Method | `setUseGradient` | `useGradient`: bool | `null`: null |
| | | Method | `getUseGradient` | None | `bool`: bool |
| | | Method | `setColors` | `argbCols`: uint[], `positions`: double[], `colNames`: string[], `useGradient`: optional<bool> | `null`: null |
| | | Method | `setColorAtIndex` | `index`: int, `red`: int, `green`: int, `blue`: int, `alpha`: int, `position`: double, `name`: string, `useGradient`: optional<bool> | `null`: null |
| | | Method | `getColorAtIndex` | `colorIndex`: int | `int`: int |
| | | Method | `getColorPositionAtIndex` | `colorIndex`: int | `double`: double |
| | | Method | `launchVirtualWorld` | `action`: string | `null`: null |
| | | Method | `getUnrealWorld` | None | `handle`: handle |
| | | Method | `setMultiResourceItemRestrictedServiceIps` | `itemIndex`: int, `ipAdresses`: string[] | `null`: null |
| | | Method | `getMultiResourceItemRestrictedServiceIps` | `itemIndex`: int | `string[]`: string[] |
| | | Method | `replace` | `path`: string | `null`: null |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| | | Method | `transcodeWithExisitngPreset` | `presetName`: string, `useRxCache`: bool, `destinationPath`: string, `startFrame`: int, `endFrame`: int, `serviceId`: uint | `null`: null |
| | | Method | `transcodeWithSettings` | `settings`: string, `useRxCache`: bool, `destinationPath`: string, `startFrame`: int, `endFrame`: int, `serviceId`: uint | `null`: null |
| | | Method | `moveToTranscodingFolder` | `folderPath`: string | `null`: null |
| Resources | Class | | `UnrealWorld` | | |
| | | Method | `getLevelNames` | None | `string[]`: string[] |
| | | Method | `loadLevel` | `levelName`: string | `null`: null |
| | | Method | `getEventTriggerNames` | None | `string[]`: string[] |
| | | Method | `triggerEventByName` | `triggerName`: string | `null`: null |
| | | Method | `createNDisplayConfig` | None | `null`: null |
| | | Method | `runUnreal` | None | `null`: null |
| | | Method | `killUnreal` | None | `null`: null |
| | | Method | `getName` | None | `string`: string |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Timelines | Function | | `getTimelineAtIndex` | `index`: int | `handle`: handle |
| Timelines | Function | | `getTimelineFromName` | `name`: string | `handle`: handle |
| Timelines | Function | | `getTimelines` | None | `handle[]`: handle[] |
| Timelines | Function | | `getTimelineNames` | None | `string[]`: string[] |
| Timelines | Function | | `getTimelinesSelected` | None | `handle[]`: handle[] |
| Timelines | Function | | `createTimeline` | None | `handle`: handle |
| Timelines | Function | | `getNodeFromId` | `id`: double | `handle`: handle |
| Timelines | Class | | `Timeline` | | |
| | | Method | `ref` | None | `handle`: handle |
| | | Method | `removeThis` | None | `null`: null |
| | | Method | `duplicateThis` | `withoutClipsCues`: optional<bool> | `handle`: handle |
| | | Method | `selectThis` | None | `null`: null |
| | | Method | `getZoomFactor` | None | `double`: double |
| | | Method | `setZoomFactor` | `zoomFactor`: double | `null`: null |
| | | Method | `getVerticalScrollOffset` | None | `int`: int |
| | | Method | `setVerticalScrollOffset` | `offset`: int | `null`: null |
| | | Method | `getHorizontalScrollOffset` | None | `int`: int |
| | | Method | `setHorizontalScrollOffset` | `offset`: int | `null`: null |
| | | Method | `moveInRenderOrder` | `moveDown`: bool | `null`: null |
| | | Method | `getLayers` | None | `handle[]`: handle[] |
| | | Method | `getLayerNames` | None | `string[]`: string[] |
| | | Method | `getLayersSelected` | None | `handle[]`: handle[] |
| | | Method | `selectLayerByIndex` | `index`: int | `null`: null |
| | | Method | `selectLayerByNames` | `layerNames`: string[] | `null`: null |
| | | Method | `getLayerAtIndex` | `index`: int | `handle`: handle |
| | | Method | `createLayer` | None | `handle`: handle |
| | | Method | `getCueInfosAsJsonString` | None | `string`: string |
| | | Method | `getCues` | None | `handle[]`: handle[] |
| | | Method | `getCueNames` | None | `string[]`: string[] |
| | | Method | `getCueAtIndex` | `index`: int | `handle`: handle |
| | | Method | `getCueFromName` | `name`: string | `handle`: handle |
| | | Method | `getCueFromNumber` | `number`: int | `handle`: handle |
| | | Method | `applyCueWithName` | `name`: string | `null`: null |
| | | Method | `applyCueWithNumber` | `number`: int | `null`: null |
| | | Method | `createCue` | `name`: string, `timeInFrames`: double, `operation`: int | `handle`: handle |
| | | Method | `removeCues` | None | `null`: null |
| | | Method | `createPauseCueBeforeSelectedClips` | None | `null`: null |
| | | Method | `play` | None | `null`: null |
| | | Method | `pause` | None | `null`: null |
| | | Method | `stop` | None | `null`: null |
| | | Method | `toggleTransport` | None | `null`: null |
| | | Method | `store` | None | `null`: null |
| | | Method | `reset` | None | `null`: null |
| | | Method | `getAttributes` | None | `TimelineAttributes`: TimelineAttributes |
| | | Method | `setCurrentFrame` | `time`: int | `bool`: bool |
| | | Method | `setCurrentTime` | `time`: int | `null`: null |
| | | Method | `getCurrentTime` | None | `int`: int |
| | | Method | `scrubCurrentTime` | `frames`: int | `null`: null |
| | | Method | `CurrentTime` | `time`: int, `doSet`: bool | `int`: int |
| | | Method | `getCurrentHMSF` | None | `string`: string |
| | | Method | `setTransportMode` | `mode`: int | `bool`: bool |
| | | Method | `getTransportMode` | None | `int`: int |
| | | Method | `setTimecodeInput` | `hour`: int, `minute`: int, `second`: int, `frame`: int, `elapsedTime`: double, `running`: bool, `freshMode`: int, `stateToken`: int, `format`: int | `double`: double |
| | | Method | `getFps` | None | `double`: double |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setName` | `name`: string | `null`: null |
| | | Method | `moveToNextCue` | None | `null`: null |
| | | Method | `moveToNextCueIgnoreProperties` | None | `null`: null |
| | | Method | `getCueNext` | None | `handle`: handle |
| | | Method | `moveToPreviousCue` | None | `null`: null |
| | | Method | `moveToPreviousCueIgnoreProperties` | None | `null`: null |
| | | Method | `getCuePrevious` | None | `handle`: handle |
| | | Method | `ignoreNextCue` | None | `null`: null |
| | | Method | `ignoreNextCueWithOperation` | `cueOperation`: int | `null`: null |
| | | Method | `blendToTime` | `goalTime`: double, `blendDuration`: double, `preloadDelayInMilliseconds`: optional<int> | `null`: null |
| | | Method | `blendToTimeWithTransportMode` | `goalTime`: double, `blendDuration`: double, `transportMode`: int, `preloadDelayInMilliseconds`: optional<int> | `null`: null |
| | | Method | `setBlendToTimeMode` | `mode`: int | `bool`: bool |
| | | Method | `setSpeedFactor` | `factor`: double | `null`: null |
| | | Method | `getSpeedFactor` | None | `double`: double |
| | | Method | `setOpacity` | `value`: double | `null`: null |
| | | Method | `getOpacity` | None | `double`: double |
| | | Method | `startOpacityAnimation` | `fadeIn`: bool, `durationFrames`: double | `null`: null |
| | | Method | `setSmpteMode` | `mode`: int | `null`: null |
| | | Method | `getSmpteMode` | None | `int`: int |
| | | Method | `storeRecordedValues` | None | `null`: null |
| | | Method | `setSmpteInputBehaviour` | `mode`: int | `null`: null |
| | | Method | `getSmpteInputBehaviour` | None | `int`: int |
| | | Method | `setSmpteOffset` | `time`: double | `null`: null |
| | | Method | `getSmpteOffset` | None | `double`: double |
| | | Method | `resetRecordedValues` | None | `null`: null |
| | | Method | `getTimelineInfosAsJsonString` | None | `string`: string |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Timelines | Class | | `Layer` | | |
| | | Method | `ref` | None | `handle`: handle |
| | | Method | `removeThis` | None | `null`: null |
| | | Method | `getNodes` | None | `handle[]`: handle[] |
| | | Method | `getNodeWithName` | `name`: string | `handle`: handle |
| | | Method | `getParamWithName` | `name`: string | `handle`: handle |
| | | Method | `getSpatialParametersAtTime` | `time`: double | `double[]`: double[] |
| | | Method | `getTimeline` | None | `handle`: handle |
| | | Method | `setName` | `name`: string | `null`: null |
| | | Method | `getName` | None | `string`: string |
| | | Method | `resetLayer` | None | `null`: null |
| | | Method | `getLayerJsonDescrip` | None | `string`: string |
| | | Method | `setLayerJsonDescrip` | `descrip`: string, `makeAllDominant`: bool | `null`: null |
| | | Method | `getJsonDescrip` | None | `string`: string |
| | | Method | `initFromJsonDescrip` | `descrip`: string | `null`: null |
| | | Method | `setOpacity` | `value`: double | `null`: null |
| | | Method | `getOpacity` | None | `double`: double |
| | | Method | `resetOpacity` | None | `null`: null |
| | | Method | `setVolume` | `value`: double | `null`: null |
| | | Method | `getVolume` | None | `double`: double |
| | | Method | `resetVolume` | None | `null`: null |
| | | Method | `muteLayer` | None | `null`: null |
| | | Method | `unMuteLayer` | None | `null`: null |
| | | Method | `getIsLayerMuted` | None | `bool`: bool |
| | | Method | `muteAudio` | None | `null`: null |
| | | Method | `unMuteAudio` | None | `null`: null |
| | | Method | `getIsAudioMuted` | None | `bool`: bool |
| | | Method | `getDmxMuteState` | None | `int`: int |
| | | Method | `setDmxMuteState` | `muteState`: uint | `null`: null |
| | | Method | `toggleExplicitMute` | `flag`: uint | `null`: null |
| | | Method | `setTransport` | `mode`: int, `loop`: bool | `null`: null |
| | | Method | `getTransportMode` | None | `int`: int |
| | | Method | `resetTransportMode` | None | `null`: null |
| | | Method | `getTransportLoop` | None | `bool`: bool |
| | | Method | `assignResource` | `id`: double | `null`: null |
| | | Method | `assignResourceWithFade` | `id`: double, `fadeDuration`: double | `null`: null |
| | | Method | `getAssignedResource` | None | `handle`: handle |
| | | Method | `resetAssignedResource` | None | `null`: null |
| | | Method | `getAssignedModelResource` | None | `handle`: handle |
| | | Method | `resetAssignedModelResource` | None | `null`: null |
| | | Method | `getFxNames` | None | `string[]`: string[] |
| | | Method | `setFadeDurationDominantResourceChange` | `value`: double | `null`: null |
| | | Method | `getFadeDurationDominantResourceChange` | None | `double`: double |
| | | Method | `createClip` | None | `handle`: handle |
| | | Method | `createClipAtTime` | `timeInFrames`: double | `handle`: handle |
| | | Method | `controlClipBorder` | `clip`: handle, `isEnter`: bool, `isIncremental`: bool, `entryTime`: double | `null`: null |
| | | Method | `getClipAtIndex` | `index`: int | `handle`: handle |
| | | Method | `getClips` | None | `handle[]`: handle[] |
| | | Method | `getClipCurrent` | `offset`: int | `handle`: handle |
| | | Method | `getClipsSelected` | None | `handle[]`: handle[] |
| | | Method | `removeClips` | None | `null`: null |
| | | Method | `setHomeScreenFromScreenName` | `screenName`: string | `null`: null |
| | | Method | `getHomeScreenName` | None | `string`: string |
| | | Method | `setBlendMode` | `blendMode`: string | `null`: null |
| | | Method | `getBlendMode` | None | `string`: string |
| | | Method | `addEffectById` | `id`: double | `null`: null |
| | | Method | `setPreloadPermanently` | `doPreloadPermanently`: bool | `null`: null |
| | | Method | `getPreloadPermanently` | None | `bool`: bool |
| | | Method | `setRestrictToServiceWithIps` | `doRestrict`: bool, `ipAdresses`: string[] | `null`: null |
| | | Method | `getRestrictToService` | None | `bool`: bool |
| | | Method | `getRestrictedServiceIps` | None | `string[]`: string[] |
| | | Method | `getOffsets` | None | `double[]`: double[] |
| | | Method | `setOffsets` | `x`: optional<double>, `y`: optional<double>, `z`: optional<double>, `xr`: optional<double>, `yr`: optional<double>, `zr`: optional<double>, `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | `null`: null |
| | | Method | `setCurrentValuesToOffset` | `typeIndex`: int, `resetDominant`: optional<bool>, `removeKeyframesClips`: optional<bool> | `null`: null |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Timelines | Class | | `Clip` | | |
| | | Method | `getId` | None | `double`: double |
| | | Method | `removeThis` | None | `null`: null |
| | | Method | `getTimeline` | None | `handle`: handle |
| | | Method | `setTime` | `time`: double | `null`: null |
| | | Method | `getTime` | None | `double`: double |
| | | Method | `setDuration` | `duration`: double | `null`: null |
| | | Method | `getDuration` | None | `double`: double |
| | | Method | `setLabel` | `label`: string | `null`: null |
| | | Method | `getLabel` | None | `string`: string |
| | | Method | `getPlayMode` | None | `int`: int |
| | | Method | `setPlayMode` | `playMode`: int | `null`: null |
| | | Method | `getSpeed` | None | `double`: double |
| | | Method | `setSpeed` | `speed`: double | `null`: null |
| | | Method | `getBlendFrames` | None | `bool`: bool |
| | | Method | `setBlendFrames` | `doFrameblending`: bool | `null`: null |
| | | Method | `getInpoint` | None | `double`: double |
| | | Method | `setInpoint` | `inpoint`: double | `null`: null |
| | | Method | `getOutpoint` | None | `double`: double |
| | | Method | `setOutpoint` | `inpoint`: double | `null`: null |
| | | Method | `assignResource` | `resId`: double, `setToResourceDuration`: optional<bool> | `null`: null |
| | | Method | `getAssignedResource` | None | `handle`: handle |
| | | Method | `setToResourceDuration` | None | `null`: null |
| | | Method | `createEvent` | `namePath`: string, `time`: double, `value`: double | `null`: null |
| | | Method | `createEventInPixelSpace` | `namePath`: string, `time`: double, `value`: double | `null`: null |
| | | Method | `removeEvent` | `namePath`: string, `time`: double | `null`: null |
| | | Method | `createPauseCueBeforeClip` | None | `handle`: handle |
| | | Method | `setColorTransformPath` | `colorTransformPath`: string | `null`: null |
| | | Method | `getColorTransformPath` | None | `string`: string |
| | | Method | `clearColorTransformPath` | None | `null`: null |
| | | Method | `getKeyframesAsJsonString` | None | `string`: string |
| Timelines | Class | | `Node` | | |
| | | Method | `getParameters` | None | `handle[]`: handle[] |
| | | Method | `getName` | None | `string`: string |
| | | Method | `getParamWithName` | `name`: string | `handle`: handle |
| | | Method | `setValues` | `values`: double[] | `null`: null |
| | | Method | `getValues` | None | `double[]`: double[] |
| | | Method | `resetValues` | None | `null`: null |
| | | Method | `storeValues` | None | `null`: null |
| | | Method | `mute` | None | `null`: null |
| | | Method | `unMute` | None | `null`: null |
| | | Method | `getIsMuted` | None | `bool`: bool |
| | | Method | `getTimeline` | None | `handle`: handle |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Timelines | Class | | `Param` | | |
| | | Method | `getName` | None | `string`: string |
| | | Method | `getIsChannel` | None | `bool`: bool |
| | | Method | `setValue` | `value`: timelineParamValue | `null`: null |
| | | Method | `setValueRelativ` | `value`: double | `null`: null |
| | | Method | `getValue` | None | `timelineParamValue`: timelineParamValue |
| | | Method | `resetValue` | None | `null`: null |
| | | Method | `storeValue` | None | `null`: null |
| | | Method | `setTransportAttributes` | `mode`: int, `speed`: double, `loop`: bool, `inpoint`: int, `outpoint`: int | `null`: null |
| | | Method | `getAttributes` | None | `TransportAttributes`: TransportAttributes |
| | | Method | `mute` | None | `null`: null |
| | | Method | `unMute` | None | `null`: null |
| | | Method | `getIsMuted` | None | `bool`: bool |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Timelines | Class | | `Cue` | | |
| | | Method | `removeThis` | None | `null`: null |
| | | Method | `apply` | None | `null`: null |
| | | Method | `blendToThis` | `blendDurationInSeconds`: double | `null`: null |
| | | Method | `getAttributes` | None | `CueAttributes`: CueAttributes |
| | | Method | `getTimeline` | None | `handle`: handle |
| | | Method | `getIndex` | None | `int`: int |
| | | Method | `getName` | None | `string`: string |
| | | Method | `setName` | `name`: string | `bool`: bool |
| | | Method | `getNote` | None | `string`: string |
| | | Method | `setNote` | `note`: string | `bool`: bool |
| | | Method | `getOperation` | None | `int`: int |
| | | Method | `setOperation` | `operation`: int | `bool`: bool |
| | | Method | `getJumpMode` | None | `int`: int |
| | | Method | `setJumpMode` | `jumpMode`: int | `bool`: bool |
| | | Method | `getJumpGoalTime` | None | `double`: double |
| | | Method | `setJumpGoalTime` | `time`: double | `bool`: bool |
| | | Method | `getJumpGoalLabel` | None | `string`: string |
| | | Method | `getJumpGoalCue` | None | `handle`: handle |
| | | Method | `setJumpGoalLabel` | `jumpGoalLabel`: string | `bool`: bool |
| | | Method | `getNumber` | None | `int`: int |
| | | Method | `setNumber` | `number`: int | `null`: null |
| | | Method | `getWaitDuration` | None | `double`: double |
| | | Method | `setWaitDuration` | `time`: double | `bool`: bool |
| | | Method | `getBlendDuration` | None | `double`: double |
| | | Method | `setBlendDuration` | `timeInFrames`: double | `bool`: bool |
| | | Method | `getTime` | None | `double`: double |
| | | Method | `setTime` | `time`: double | `bool`: bool |
| | | Method | `getTimelineToTriggerName` | None | `string`: string |
| | | Method | `setTimelineToTrigger` | `nameTimeline`: string | `bool`: bool |
| | | Method | `getTimelineTriggerMode` | None | `int`: int |
| | | Method | `setTimelineTriggerMode` | `mode`: int | `bool`: bool |
| | | Method | `getTimelineTriggerApplyTime` | None | `double`: double |
| | | Method | `setTimelineTriggerApplyTime` | `time`: double | `bool`: bool |
| | | Method | `setTimelineTriggerApplyCue` | `goalCueLabel`: string | `bool`: bool |
| | | Method | `getCountdown` | None | `double`: double |
| | | Method | `getCountdownHMSF` | None | `string`: string |
| | | Method | `setCommand` | `conveyorName`: string, `commandData`: string | `null`: null |
| | | Method | `getInst` | `instancePath`: string | `handle`: handle |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | `handle`: handle |
| | | Method | `getInstancePath` | None | `string`: string |
| Calibration | Function | | `setMarkerPositions` | `positions`: double[], `markerIds`: int[] | `null`: null |
| WebViews | Function | | `loadDeviceUi` | `devicePath`: string | `null`: null |
| WebViews | Function | | `activatePreviousFunc` | None | `null`: null |
| WebViews | Function | | `activateNextFunc` | None | `null`: null |
| WebViews | Function | | `getLastActivatedFunc` | None | `string`: string |
| WebViews | Function | | `deviceActivated` | `devicePath`: string, `withSelection`: bool | `null`: null |
| WebViews | Function | | `funcActivated` | `funcPath`: string, `withSelection`: bool | `null`: null |
| WebViews | Function | | `setFuncBodyState` | `funcPath`: string, `state`: string | `null`: null |
| WebViews | Function | | `getFuncBodyState` | `funcPath`: string | `string`: string |
| WebViews | Function | | `setTag` | `tag`: string, `text`: string | `null`: null |
| WebViews | Function | | `setEditorIsUsingBlocks` | `useBlocks`: bool | `null`: null |
| Ui | Function | | `getComboBoxWithId` | `id`: double | `handle`: handle |
| Ui | Function | | `setAppMode` | `mode`: int | `null`: null |
| Ui | Function | | `getAppMode` | None | `int`: int |
| Ui | Function | | `getDisplayTestpattern` | None | `bool`: bool |
| Ui | Function | | `setDisplayTestpattern` | `display`: bool | `null`: null |
| Ui | Function | | `getPreviewCameraAsJsonString` | None | `string`: string |
| Ui | Function | | `setPreviewCameraAsJsonString` | `cameraFrustrumStateString`: string | `null`: null |
| Ui | Function | | `setDisableContentRendering` | `state`: bool | `null`: null |
| Ui | Function | | `getIsContentRenderingDisabled` | None | `bool`: bool |
| Ui | Function | | `setDisableWorkspaceRendering` | `state`: bool | `null`: null |
| Ui | Function | | `getIsWorkspaceRenderingDisabled` | None | `bool`: bool |
| Ui | Class | | `ComboBox` | | |
| | | Method | `clear` | None | `null`: null |
| | | Method | `addItem` | `item`: string, `id`: int | `null`: null |
| | | Method | `setSelectedId` | `id`: int | `null`: null |
| | | Method | `getSelectedId` | None | `int`: int |
| Direct | Function | | `setRegistered` | `hdls`: handle[], `expectedFrequency`: int, `dampingMs`: int, `usageHints`: string[] | `null`: null |
| Direct | Function | | `reloadRegistered` | None | `null`: null |
| Direct | Function | | `registerScreen` | `name`: string, `expectedFrequency`: int, `dampingMs`: int | `handle`: handle |
| Direct | Function | | `registerParam` | `instancePath`: string | `handle`: handle |
| Direct | Function | | `registerCamera` | `cameraName`: string, `expectedFrequency`: int | `handle`: handle |
| Direct | Function | | `registerPerspective` | `screenName`: string, `expectedFrequency`: int | `handle`: handle |
| Direct | Class | | `Screen` | | |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | `null`: null |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `null`: null |
| | | Method | `setPosRot` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | `null`: null |
| | | Method | `setPosRotScale` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | `null`: null |
| | | Method | `enableLogging` | `enable`: bool | `null`: null |
| Direct | Class | | `Param` | | |
| | | Method | `setValue` | `value`: double | `null`: null |
| | | Method | `enableLogging` | `enable`: bool | `null`: null |
| Direct | Class | | `Camera` | | |
| | | Method | `setPosition` | `xPos`: double, `yPos`: double, `zPos`: double | `null`: null |
| | | Method | `setRotation` | `xRot`: double, `yRot`: double, `zRot`: double | `null`: null |
| | | Method | `setTransformation` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double | `null`: null |
| | | Method | `setTransformationAndLensProps` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `iris`: double, `k1`: double, `k2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double | `null`: null |
| | | Method | `setTransformationAndLensPropsExt` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `focalDistance`: double, `zoom`: double, `iris`: double, `k1`: double, `k2`: double, `k3`: double, `p1`: double, `p2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double, `overscan`: double | `null`: null |
| Direct | Class | | `Perspective` | | |
| | | Method | `setTransformation` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double | `null`: null |
| | | Method | `setTransformationAndLensProps` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `iris`: double, `k1`: double, `k2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double | `null`: null |
