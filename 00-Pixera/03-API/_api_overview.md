# API Overview
| Namespace | Entity | Type | Name | Parameters | Return Values |
| --- | --- | --- | --- | --- | --- |
| Utility | Function | | `getApiRevision` | None | None |
| Utility | Function | | `getHasFunction` | `functionName`: string | None |
| Utility | Function | | `outputDebug` | `message`: string | None |
| Utility | Function | | `getLicenseJson` | None | None |
| Utility | Function | | `getCurrentTime` | None | None |
| Utility | Function | | `getCurrentTimeAsString` | None | None |
| Utility | Function | | `noop` | None | None |
| Utility | Function | | `requestCallback` | `functionName`: string | None |
| Utility | Function | | `readFileString` | `path`: string | None |
| Utility | Function | | `writeFileString` | `path`: string, `fileStr`: string | None |
| Utility | Function | | `getAccessRecipe` | `hdlPath`: string | None |
| Utility | Function | | `pollMonitoring` | None | None |
| Utility | Function | | `unsubscribeMonitoringSubject` | `subject`: string | None |
| Utility | Function | | `subscribeMonitoringSubject` | `subject`: string | None |
| Utility | Function | | `setMonitoringEventMode` | `mode`: string | None |
| Utility | Function | | `monitoringEvent` | `eventDescription`: string | None |
| Utility | Function | | `setShowContextInReplies` | `doShow`: bool | None |
| Utility | Function | | `setMonitoringHasDelimiter` | `hasDelimiter`: bool | None |
| Utility | Function | | `runJsScript` | `jsFunction`: string, `jsCode`: string | None |
| Utility | Function | | `dynamicRebuildFromJsonDescription` | `deviceName`: string, `jsonDescription`: string, `folder`: string | None |
| Network | Function | | `getConveyor` | `conveyorName`: string | None |
| Network | Class | | `Conveyor` | | |
| | | Method | `sendString` | `str`: string | None |
| Compound | Function | | `setTransportModeOnTimelineAtIndex` | `index`: int, `mode`: int | None |
| Compound | Function | | `setTransportModeOnTimeline` | `timelineName`: string, `mode`: int | None |
| Compound | Function | | `toggleTransport` | `timelineName`: string | None |
| Compound | Function | | `getTransportModeOnTimeline` | `timelineName`: string | None |
| Compound | Function | | `setOpacityOnTimeline` | `timelineName`: string, `opacity`: double | None |
| Compound | Function | | `getOpacityOnTimeline` | `timelineName`: string | None |
| Compound | Function | | `startFirstTimeline` | None | None |
| Compound | Function | | `pauseFirstTimeline` | None | None |
| Compound | Function | | `stopFirstTimeline` | None | None |
| Compound | Function | | `setPosValue` | `val`: double | None |
| Compound | Function | | `setPosValueXY` | `valX`: double, `valY`: double | None |
| Compound | Function | | `setParamValue` | `path`: string, `value`: double | None |
| Compound | Function | | `applyCueAtIndexOnTimelineAtIndex` | `cueIndex`: int, `timelineIndex`: int | None |
| Compound | Function | | `applyCueNumberOnTimelineAtIndex` | `cueNumber`: int, `timelineIndex`: int | None |
| Compound | Function | | `applyCueNumberOnTimeline` | `timelineName`: string, `cueNumber`: int | None |
| Compound | Function | | `applyCueOnTimeline` | `timelineName`: string, `cueName`: string | None |
| Compound | Function | | `addResourceToFolder` | `namePath`: string, `filePath`: string | None |
| Compound | Function | | `assignResourceToLayer` | `resourcePath`: string, `layerPath`: string | None |
| Compound | Function | | `refreshResource` | `resourcePath`: string | None |
| Compound | Function | | `setTransportModeOnLayer` | `layerPath`: string, `mode`: int, `loop`: bool | None |
| Compound | Function | | `getTransportModeOnLayer` | `layerPath`: string | None |
| Compound | Function | | `getResourceAssignedToLayer` | `layerPath`: string | None |
| Compound | Function | | `assignResourceToClipAtTimeByDmxId` | `layerPath`: string, `dmxFolderId`: int, `dmxFileId`: int, `time`: double | None |
| Compound | Function | | `assignResourceToClipAtHMSFStringByDmxId` | `layerPath`: string, `dmxFolderId`: int, `dmxFileId`: int, `hmsf`: string | None |
| Compound | Function | | `assignResourceToClipAtHMSFByDmxId` | `layerPath`: string, `dmxFolderId`: int, `dmxFileId`: int, `h`: int, `m`: int, `s`: int, `f`: int | None |
| Compound | Function | | `setCurrentTimeOfTimeline` | `timelineName`: string, `time`: int | None |
| Compound | Function | | `setCurrentTimeOfTimelineInSeconds` | `timelineName`: string, `time`: double | None |
| Compound | Function | | `setCurrentTimeAndTransportModeOfTimelineInSeconds` | `timelineName`: string, `time`: double, `mode`: int | None |
| Compound | Function | | `getFpsOfTimeline` | `timelineName`: string | None |
| Compound | Function | | `getCurrentTimeOfTimeline` | `timelineName`: string | None |
| Compound | Function | | `getCurrentTimeOfTimelineInSeconds` | `timelineName`: string | None |
| Compound | Function | | `getCurrentHMSFOfTimeline` | `timelineName`: string | None |
| Compound | Function | | `getCurrentCountdownOfTimeline` | `timelineName`: string | None |
| Compound | Function | | `getCurrentCountdownHMSFOfTimeline` | `timelineName`: string | None |
| Compound | Function | | `startOpacityAnimationOfTimeline` | `timelineName`: string, `fadeIn`: bool, `fullFadeDuration`: double | None |
| Compound | Function | | `createClipOnLayerAtTimeWithResource` | `layerPath`: string, `time`: double, `resourcePath`: string | None |
| Compound | Function | | `removeClipOnLayerWithIndex` | `layerPath`: string, `clipIndex`: int | None |
| Compound | Function | | `removeAllClipsOnLayer` | `layerPath`: string | None |
| Compound | Function | | `getClipDurationInSecondsWithIndex` | `layerPath`: string, `clipIndex`: int | None |
| Compound | Function | | `getClipDurationInFramesWithIndex` | `layerPath`: string, `clipIndex`: int | None |
| Compound | Function | | `getClipTimeInSecondsWithIndex` | `layerPath`: string, `clipIndex`: int | None |
| Compound | Function | | `getClipEndTimeInSecondsWithIndex` | `layerPath`: string, `clipIndex`: int | None |
| Compound | Function | | `getResourceDurationInSeconds` | `resourcePath`: string | None |
| Compound | Function | | `getParamValue` | `path`: string | None |
| Compound | Function | | `setTimecodeInput` | `hour`: int, `minute`: int, `second`: int, `frame`: int, `elapsedTime`: double, `running`: bool, `freshMode`: int, `stateToken`: int, `format`: int | None |
| Compound | Function | | `takeOverAllClients` | None | None |
| Compound | Function | | `setPauseSmpteInput` | `doPause`: bool | None |
| Session | Function | | `closeApp` | `saveProject`: bool | None |
| Session | Function | | `loadProject` | `path`: string | None |
| Session | Function | | `saveProject` | None | None |
| Session | Function | | `saveProjectAs` | `path`: string | None |
| Session | Function | | `getProjectName` | None | None |
| Session | Function | | `setProjectName` | `name`: string | None |
| Session | Function | | `getProjectDirectory` | None | None |
| Session | Function | | `getControlMultiUserSessionName` | None | None |
| Session | Function | | `shutdownSystem` | `mode`: optional<int> | None |
| Session | Function | | `getLiveSystemIps` | None | None |
| Session | Function | | `getLiveSystemState` | `ip`: string | None |
| Session | Function | | `liveSystemStateChange` | `ip`: string, `state`: string | None |
| Session | Function | | `shutdownLiveSystem` | `ip`: string, `mode`: optional<int> | None |
| Session | Function | | `wakeLiveSystem` | `ip`: string | None |
| Session | Function | | `getLiveSystemMacAddress` | `ip`: string | None |
| Session | Function | | `startLiveSystem` | `ip`: string | None |
| Session | Function | | `startLiveSystems` | None | None |
| Session | Function | | `stopLiveSystem` | `ip`: string | None |
| Session | Function | | `stopLiveSystems` | None | None |
| Session | Function | | `restartLiveSystem` | `ip`: string | None |
| Session | Function | | `restartLiveSystems` | None | None |
| Session | Function | | `remoteSystemStateChange` | `ip`: string, `state`: string | None |
| Session | Function | | `getRemoteSystemIps` | None | None |
| Session | Function | | `getRemoteSystemState` | `ip`: string | None |
| Session | Function | | `setVideoStreamActiveState` | `ip`: string, `device`: string, `isActive`: bool | None |
| Session | Function | | `getVideoStreamActiveState` | `ip`: string, `device`: string | None |
| Session | Function | | `getDefaultClipDurationsAsJsonString` | None | None |
| LiveSystems | Function | | `getLiveSystems` | None | None |
| LiveSystems | Function | | `liveSystemNotAvailable` | `reason`: int, `system`: handle | None |
| LiveSystems | Function | | `getMultiUserMembers` | None | None |
| LiveSystems | Class | | `MultiUserMember` | | |
| | | Method | `getName` | None | None |
| | | Method | `getIp` | None | None |
| | | Method | `getState` | None | None |
| | | Method | `getPerformanceMonitoringValuesJson` | None | None |
| | | Method | `getPerformanceMonitoringValuesJsonEx` | `filter`: string | None |
| | | Method | `resetCumulativePerformanceMonitoringValues` | None | None |
| | | Method | `ensureFileDistribution` | `includeNotUsedYet`: bool | None |
| | | Method | `shutDown` | `mode`: int | None |
| | | Method | `wakeUp` | None | None |
| | | Method | `getMacAddress` | None | None |
| | | Method | `resetEngine` | None | None |
| | | Method | `restartEngine` | None | None |
| | | Method | `startEngine` | None | None |
| | | Method | `closeEngine` | None | None |
| | | Method | `triggerBackup` | `applyControlCommand`: optional<bool> | None |
| | | Method | `getStructureJson` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| LiveSystems | Class | | `LiveSystem` | | |
| | | Method | `getName` | None | None |
| | | Method | `getIp` | None | None |
| | | Method | `getState` | None | None |
| | | Method | `setBackupRole` | `role`: int | None |
| | | Method | `getBackupRole` | None | None |
| | | Method | `getPerformanceMonitoringValuesJson` | None | None |
| | | Method | `getPerformanceMonitoringValuesJsonEx` | `filter`: string | None |
| | | Method | `resetCumulativePerformanceMonitoringValues` | None | None |
| | | Method | `moveMappingsToOutputs` | `hdlSrc`: handle, `outputIdPathMapStr`: string | None |
| | | Method | `clearExportedMappings` | `path`: string, `onlyServicePath`: bool | None |
| | | Method | `exportMappings` | `path`: string | None |
| | | Method | `importMappings` | `path`: string, `outputIdPathMapStr`: string | None |
| | | Method | `exportMappingsDirectly` | `path`: string | None |
| | | Method | `importMappingsDirectly` | `path`: string, `outputIdPathMapStr`: string | None |
| | | Method | `exportMappingsToLiveSystemPath` | `parentPath`: string | None |
| | | Method | `importMappingsFromLiveSystemPath` | `parentPath`: string | None |
| | | Method | `clearExportedMappingsAtLiveSystemPath` | `path`: string | None |
| | | Method | `ensureFileDistribution` | `includeNotUsedYet`: bool | None |
| | | Method | `shutDown` | `mode`: int | None |
| | | Method | `wakeUp` | None | None |
| | | Method | `getMacAddress` | None | None |
| | | Method | `getGraphicsDevices` | None | None |
| | | Method | `getEnabledOutputs` | None | None |
| | | Method | `getAllOutputs` | None | None |
| | | Method | `getVideoStreamOutputs` | None | None |
| | | Method | `resetEngine` | None | None |
| | | Method | `restartEngine` | None | None |
| | | Method | `startEngine` | None | None |
| | | Method | `closeEngine` | None | None |
| | | Method | `setAudioMasterVolume` | `channel`: int, `volume`: double | None |
| | | Method | `getAudioMasterVolume` | `channel`: int | None |
| | | Method | `setAudioMasterMute` | `channel`: int, `state`: bool | None |
| | | Method | `getAudioMasterMute` | `channel`: int | None |
| | | Method | `setAudioTimecodeInput` | `channel`: int, `state`: bool | None |
| | | Method | `triggerBackup` | `applyControlCommand`: optional<bool> | None |
| | | Method | `getStructureJson` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| LiveSystems | Class | | `GraphicsDevice` | | |
| | | Method | `getName` | None | None |
| | | Method | `getEnabledOutputs` | None | None |
| | | Method | `getAllOutputs` | None | None |
| LiveSystems | Class | | `Output` | | |
| | | Method | `getName` | None | None |
| | | Method | `setActive` | `active`: bool | None |
| | | Method | `getActive` | None | None |
| | | Method | `setIdentify` | `state`: bool | None |
| | | Method | `getIdentify` | None | None |
| | | Method | `getAssignedScreens` | None | None |
| | | Method | `getAssignedProjectors` | None | None |
| | | Method | `getEnabled` | None | None |
| | | Method | `getForPreview` | None | None |
| LiveSystems | Class | | `VideoStream` | | |
| | | Method | `getName` | None | None |
| | | Method | `setActive` | `active`: bool | None |
| | | Method | `getActive` | None | None |
| Screens | Function | | `getScreenWithName` | `name`: string | None |
| Screens | Function | | `setNamedScreenPosition` | `name`: string, `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| Screens | Function | | `getScreens` | None | None |
| Screens | Function | | `getScreenNames` | None | None |
| Screens | Function | | `getFirstTimelineWithHomeScreen` | `screenName`: string | None |
| Screens | Function | | `getStudioCameras` | None | None |
| Screens | Class | | `Screen` | | |
| | | Method | `getId` | None | None |
| | | Method | `getName` | None | None |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `getPosition` | None | None |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `getRotation` | None | None |
| | | Method | `setScale` | `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | None |
| | | Method | `getScale` | None | None |
| | | Method | `setPosRot` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `setPosRotScale` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | None |
| | | Method | `getPersepective` | None | None |
| | | Method | `snapPerspectiveCornersToScreen` | `mode`: int | None |
| | | Method | `setPerspectivePosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `setPerspectivePositionWithLookAt` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `getPerspectivePosition` | None | None |
| | | Method | `setPerspectiveRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `getPerspectiveRotation` | None | None |
| | | Method | `setCameraPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `setCameraPositionWithLookAt` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `getCameraPosition` | None | None |
| | | Method | `setCameraRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `getCameraRotation` | None | None |
| | | Method | `setContentSamplingFrustumBase` | `x`: double, `y`: double, `width`: double, `height`: double, `rotation`: double, `originScreenId`: double | None |
| | | Method | `runCalibration` | `mode`: string, `diff`: string | None |
| | | Method | `editCalibration` | `diff`: string | None |
| | | Method | `resetWarpFile` | `diff`: string | None |
| | | Method | `loadWarpFile` | `filePath`: string | None |
| | | Method | `loadWarpFileWithDiff` | `filePath`: string, `diff`: string | None |
| | | Method | `addWarpFile` | `filePath`: string | None |
| | | Method | `addWarpFileWithDiff` | `filePath`: string, `diff`: string | None |
| | | Method | `loadColorCalibration` | `calibrationName`: string | None |
| | | Method | `runColorCalibration` | None | None |
| | | Method | `setIsVisible` | `isVisible`: bool | None |
| | | Method | `getIsVisible` | None | None |
| | | Method | `setIsProjectable` | `isProjectable`: bool | None |
| | | Method | `getIsProjectable` | None | None |
| | | Method | `triggerRefreshMapping` | None | None |
| | | Method | `resetAllColorCorrections` | None | None |
| | | Method | `setColorCorrectionWithPath` | `path`: string, `value`: float | None |
| | | Method | `getColorCorrectionWithPath` | `path`: string | None |
| | | Method | `setColorCorrectionAsJsonString` | `colorCorrection`: string | None |
| | | Method | `getColorCorrectionAsJsonString` | None | None |
| | | Method | `getOutput` | None | None |
| | | Method | `setBlackout` | `isActive`: bool | None |
| | | Method | `getBlackout` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Screens | Class | | `StudioCamera` | | |
| | | Method | `getName` | None | None |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `getPosition` | `xPos`: double, `yPos`: double, `zPos`: double | None |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `getRotation` | `xPos`: double, `yPos`: double, `zPos`: double | None |
| | | Method | `setTransformation` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `fov`: optional<double>, `aspectRatio`: optional<double> | None |
| | | Method | `setTransformationAndLensProps` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `iris`: double, `k1`: double, `k2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double | None |
| | | Method | `setTransformationAndLensPropsExt` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `focalDistance`: double, `zoom`: double, `iris`: double, `k1`: double, `k2`: double, `k3`: double, `p1`: double, `p2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double, `overscan`: double | None |
| | | Method | `setTrackingInputPause` | `pause`: bool | None |
| | | Method | `getTrackingInputPause` | None | None |
| | | Method | `setUsePositionPropertiesFromTracking` | `pause`: bool | None |
| | | Method | `getUsePositionPropertiesFromTracking` | None | None |
| | | Method | `setUseRotationPropertiesFromTracking` | `pause`: bool | None |
| | | Method | `getUseRotationPropertiesFromTracking` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Screens | Class | | `Perspective` | | |
| | | Method | `getName` | None | None |
| | | Method | `setTransformation` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `fov`: optional<double>, `aspectRatio`: optional<double> | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Projectors | Function | | `getProjectorWithName` | `name`: string | None |
| Projectors | Function | | `getProjectors` | None | None |
| Projectors | Function | | `getProjectorNames` | None | None |
| Projectors | Class | | `Projector` | | |
| | | Method | `getPosition` | None | None |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `getRotation` | None | None |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `getName` | None | None |
| | | Method | `activateScreenMapping` | `screenId`: double, `isActive`: bool | None |
| | | Method | `setBlackout` | `isActive`: bool | None |
| | | Method | `getBlackout` | None | None |
| | | Method | `setSoftedgeVisible` | `screenName`: string, `visible`: bool | None |
| | | Method | `resetAllColorCorrections` | None | None |
| | | Method | `setColorCorrectionWithPath` | `path`: string, `value`: float | None |
| | | Method | `getColorCorrectionWithPath` | `path`: string | None |
| | | Method | `setColorCorrectionAsJsonString` | `colorCorrection`: string | None |
| | | Method | `getColorCorrectionAsJsonString` | None | None |
| | | Method | `getOutput` | None | None |
| | | Method | `setOutput` | `outputHandle`: handle | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Resources | Function | | `getResources` | None | None |
| Resources | Function | | `getResourceFolderWithNamePath` | `namePath`: string | None |
| Resources | Function | | `getResourceFolders` | None | None |
| Resources | Function | | `getTranscodingFolders` | None | None |
| Resources | Function | | `getJsonDescrip` | None | None |
| Resources | Class | | `ResourceFolder` | | |
| | | Method | `ref` | None | None |
| | | Method | `getName` | None | None |
| | | Method | `setName` | `name`: string | None |
| | | Method | `getResourceFolders` | None | None |
| | | Method | `getResources` | None | None |
| | | Method | `getResourceAtIndex` | `index`: int | None |
| | | Method | `addResource` | `path`: string | None |
| | | Method | `addResourcesFromDirectory` | `path`: string, `removeOthers`: bool, `checkRedundancy`: bool | None |
| | | Method | `addResourcesFromDirectoryRemoveAssets` | `path`: string, `removeOthers`: bool, `checkRedundancy`: bool | None |
| | | Method | `addInternalResource` | `signature`: string, `resKind`: int | None |
| | | Method | `createFoldersFrom` | `path`: string | None |
| | | Method | `refreshResources` | None | None |
| | | Method | `moveResourceToThis` | `id`: double | None |
| | | Method | `removeThis` | None | None |
| | | Method | `removeThisIncludingAssets` | None | None |
| | | Method | `removeAllContents` | None | None |
| | | Method | `removeAllContentsIncludingAssets` | None | None |
| | | Method | `deleteAllContentsAssetsFromLiveSystem` | `apEntityLiveSystemHandle`: handle | None |
| | | Method | `resetDistributionTargets` | None | None |
| | | Method | `changeDistributionTarget` | `apEntityLiveSystemHandle`: handle, `shouldDistribute`: bool | None |
| | | Method | `replaceResourcesByString` | `searchString`: string, `replaceString`: string, `path`: string | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| | | Method | `getDmxId` | None | None |
| | | Method | `getCombinedDmxId` | None | None |
| | | Method | `setDmxId` | `id`: int | None |
| Resources | Class | | `TranscodingFolder` | | |
| | | Method | `getUsedTranscodingPreset` | None | None |
| | | Method | `setUsedTranscodingPreset` | `preset`: string | None |
| | | Method | `getTranscodeAutomatically` | None | None |
| | | Method | `setTranscodeAutomatically` | `autoTranscode`: bool | None |
| | | Method | `getUseRxCacheAsDestination` | None | None |
| | | Method | `setRxCacheAsDestination` | `useRxCache`: bool | None |
| | | Method | `getDestinationDirectory` | None | None |
| | | Method | `setDestinationDirectory` | `path`: string | None |
| Resources | Class | | `Resource` | | |
| | | Method | `ref` | None | None |
| | | Method | `removeThis` | None | None |
| | | Method | `deleteFilesOnSystems` | None | None |
| | | Method | `removeThisIncludingAssets` | None | None |
| | | Method | `deleteAssetFromLiveSystem` | `apEntityLiveSystemHandle`: handle | None |
| | | Method | `resetDistributionTargets` | None | None |
| | | Method | `changeDistributionTarget` | `apEntityLiveSystemHandle`: handle, `shouldDistribute`: bool | None |
| | | Method | `getName` | None | None |
| | | Method | `setName` | `name`: string | None |
| | | Method | `getFps` | None | None |
| | | Method | `getResolution` | None | None |
| | | Method | `getIsActive` | None | None |
| | | Method | `getVideoStreamModes` | None | None |
| | | Method | `setVideoStreamMode` | `index`: int | None |
| | | Method | `getId` | None | None |
| | | Method | `getDuration` | None | None |
| | | Method | `getType` | None | None |
| | | Method | `setCurrentVersion` | `version`: string | None |
| | | Method | `getCurrentVersion` | None | None |
| | | Method | `getVersions` | None | None |
| | | Method | `getVersionSuffix` | None | None |
| | | Method | `rescanVersions` | None | None |
| | | Method | `getThumbnailAsBase64` | None | None |
| | | Method | `getHasPendingTransfer` | None | None |
| | | Method | `getIsInUse` | None | None |
| | | Method | `getLastUsageBeginTime` | None | None |
| | | Method | `getLastUsageBeginTimeAsString` | None | None |
| | | Method | `getLastUsageEndTime` | None | None |
| | | Method | `getLastUsageEndTimeAsString` | None | None |
| | | Method | `getFilePath` | None | None |
| | | Method | `setText` | `text`: string | None |
| | | Method | `getText` | None | None |
| | | Method | `setFontWithName` | `fontName`: string | None |
| | | Method | `getFontName` | None | None |
| | | Method | `setFontWithPath` | `fontPath`: string | None |
| | | Method | `setHorizontalTextAlignment` | `textAlignment`: int | None |
| | | Method | `getHorizontalTextAlignment` | None | None |
| | | Method | `setVerticalTextAlignment` | `textAlignment`: int | None |
| | | Method | `getVerticalTextAlignment` | None | None |
| | | Method | `setLineHeight` | `lineHeight`: double | None |
| | | Method | `getLineHeight` | None | None |
| | | Method | `getTextMeasurementsWidthAndHeight` | None | None |
| | | Method | `setUrl` | `url`: string | None |
| | | Method | `getUrl` | None | None |
| | | Method | `setColorTransformPath` | `colorTransformPath`: string | None |
| | | Method | `getColorTransformPath` | None | None |
| | | Method | `clearColorTransformPath` | None | None |
| | | Method | `refresh` | `text`: string | None |
| | | Method | `distribute` | None | None |
| | | Method | `getDmxId` | None | None |
| | | Method | `setDmxId` | `id`: int | None |
| | | Method | `removeMultiresourceIndex` | `index`: int | None |
| | | Method | `addMultiresourceItem` | `id`: double | None |
| | | Method | `getMultiresourceItems` | None | None |
| | | Method | `replaceMultiresourceItemByIndex` | `index`: int, `id`: double | None |
| | | Method | `setMultiresourceResolution` | `width`: int, `height`: int | None |
| | | Method | `setMultiresourceItemSizebyIndex` | `index`: int, `width`: double, `height`: double | None |
| | | Method | `setMultiresourceItemPositionbyIndex` | `index`: int, `x`: double, `y`: double | None |
| | | Method | `setUseGradient` | `useGradient`: bool | None |
| | | Method | `getUseGradient` | None | None |
| | | Method | `setColors` | `argbCols`: uint[], `positions`: double[], `colNames`: string[], `useGradient`: optional<bool> | None |
| | | Method | `setColorAtIndex` | `index`: int, `red`: int, `green`: int, `blue`: int, `alpha`: int, `position`: double, `name`: string, `useGradient`: optional<bool> | None |
| | | Method | `getColorAtIndex` | `colorIndex`: int | None |
| | | Method | `getColorPositionAtIndex` | `colorIndex`: int | None |
| | | Method | `launchVirtualWorld` | `action`: string | None |
| | | Method | `getUnrealWorld` | None | None |
| | | Method | `setMultiResourceItemRestrictedServiceIps` | `itemIndex`: int, `ipAdresses`: string[] | None |
| | | Method | `getMultiResourceItemRestrictedServiceIps` | `itemIndex`: int | None |
| | | Method | `replace` | `path`: string | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| | | Method | `transcodeWithExisitngPreset` | `presetName`: string, `useRxCache`: bool, `destinationPath`: string, `startFrame`: int, `endFrame`: int, `serviceId`: uint | None |
| | | Method | `transcodeWithSettings` | `settings`: string, `useRxCache`: bool, `destinationPath`: string, `startFrame`: int, `endFrame`: int, `serviceId`: uint | None |
| | | Method | `moveToTranscodingFolder` | `folderPath`: string | None |
| Resources | Class | | `UnrealWorld` | | |
| | | Method | `getLevelNames` | None | None |
| | | Method | `loadLevel` | `levelName`: string | None |
| | | Method | `getEventTriggerNames` | None | None |
| | | Method | `triggerEventByName` | `triggerName`: string | None |
| | | Method | `createNDisplayConfig` | None | None |
| | | Method | `runUnreal` | None | None |
| | | Method | `killUnreal` | None | None |
| | | Method | `getName` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Timelines | Function | | `getTimelineAtIndex` | `index`: int | None |
| Timelines | Function | | `getTimelineFromName` | `name`: string | None |
| Timelines | Function | | `getTimelines` | None | None |
| Timelines | Function | | `getTimelineNames` | None | None |
| Timelines | Function | | `getTimelinesSelected` | None | None |
| Timelines | Function | | `createTimeline` | None | None |
| Timelines | Function | | `getNodeFromId` | `id`: double | None |
| Timelines | Class | | `Timeline` | | |
| | | Method | `ref` | None | None |
| | | Method | `removeThis` | None | None |
| | | Method | `duplicateThis` | `withoutClipsCues`: optional<bool> | None |
| | | Method | `selectThis` | None | None |
| | | Method | `getZoomFactor` | None | None |
| | | Method | `setZoomFactor` | `zoomFactor`: double | None |
| | | Method | `getVerticalScrollOffset` | None | None |
| | | Method | `setVerticalScrollOffset` | `offset`: int | None |
| | | Method | `getHorizontalScrollOffset` | None | None |
| | | Method | `setHorizontalScrollOffset` | `offset`: int | None |
| | | Method | `moveInRenderOrder` | `moveDown`: bool | None |
| | | Method | `getLayers` | None | None |
| | | Method | `getLayerNames` | None | None |
| | | Method | `getLayersSelected` | None | None |
| | | Method | `selectLayerByIndex` | `index`: int | None |
| | | Method | `selectLayerByNames` | `layerNames`: string[] | None |
| | | Method | `getLayerAtIndex` | `index`: int | None |
| | | Method | `createLayer` | None | None |
| | | Method | `getCueInfosAsJsonString` | None | None |
| | | Method | `getCues` | None | None |
| | | Method | `getCueNames` | None | None |
| | | Method | `getCueAtIndex` | `index`: int | None |
| | | Method | `getCueFromName` | `name`: string | None |
| | | Method | `getCueFromNumber` | `number`: int | None |
| | | Method | `applyCueWithName` | `name`: string | None |
| | | Method | `applyCueWithNumber` | `number`: int | None |
| | | Method | `createCue` | `name`: string, `timeInFrames`: double, `operation`: int | None |
| | | Method | `removeCues` | None | None |
| | | Method | `createPauseCueBeforeSelectedClips` | None | None |
| | | Method | `play` | None | None |
| | | Method | `pause` | None | None |
| | | Method | `stop` | None | None |
| | | Method | `toggleTransport` | None | None |
| | | Method | `store` | None | None |
| | | Method | `reset` | None | None |
| | | Method | `getAttributes` | None | None |
| | | Method | `setCurrentFrame` | `time`: int | None |
| | | Method | `setCurrentTime` | `time`: int | None |
| | | Method | `getCurrentTime` | None | None |
| | | Method | `scrubCurrentTime` | `frames`: int | None |
| | | Method | `CurrentTime` | `time`: int, `doSet`: bool | None |
| | | Method | `getCurrentHMSF` | None | None |
| | | Method | `setTransportMode` | `mode`: int | None |
| | | Method | `getTransportMode` | None | None |
| | | Method | `setTimecodeInput` | `hour`: int, `minute`: int, `second`: int, `frame`: int, `elapsedTime`: double, `running`: bool, `freshMode`: int, `stateToken`: int, `format`: int | None |
| | | Method | `getFps` | None | None |
| | | Method | `getName` | None | None |
| | | Method | `setName` | `name`: string | None |
| | | Method | `moveToNextCue` | None | None |
| | | Method | `moveToNextCueIgnoreProperties` | None | None |
| | | Method | `getCueNext` | None | None |
| | | Method | `moveToPreviousCue` | None | None |
| | | Method | `moveToPreviousCueIgnoreProperties` | None | None |
| | | Method | `getCuePrevious` | None | None |
| | | Method | `ignoreNextCue` | None | None |
| | | Method | `ignoreNextCueWithOperation` | `cueOperation`: int | None |
| | | Method | `blendToTime` | `goalTime`: double, `blendDuration`: double, `preloadDelayInMilliseconds`: optional<int> | None |
| | | Method | `blendToTimeWithTransportMode` | `goalTime`: double, `blendDuration`: double, `transportMode`: int, `preloadDelayInMilliseconds`: optional<int> | None |
| | | Method | `setBlendToTimeMode` | `mode`: int | None |
| | | Method | `setSpeedFactor` | `factor`: double | None |
| | | Method | `getSpeedFactor` | None | None |
| | | Method | `setOpacity` | `value`: double | None |
| | | Method | `getOpacity` | None | None |
| | | Method | `startOpacityAnimation` | `fadeIn`: bool, `durationFrames`: double | None |
| | | Method | `setSmpteMode` | `mode`: int | None |
| | | Method | `getSmpteMode` | None | None |
| | | Method | `storeRecordedValues` | None | None |
| | | Method | `setSmpteInputBehaviour` | `mode`: int | None |
| | | Method | `getSmpteInputBehaviour` | None | None |
| | | Method | `setSmpteOffset` | `time`: double | None |
| | | Method | `getSmpteOffset` | None | None |
| | | Method | `resetRecordedValues` | None | None |
| | | Method | `getTimelineInfosAsJsonString` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Timelines | Class | | `Layer` | | |
| | | Method | `ref` | None | None |
| | | Method | `removeThis` | None | None |
| | | Method | `getNodes` | None | None |
| | | Method | `getNodeWithName` | `name`: string | None |
| | | Method | `getParamWithName` | `name`: string | None |
| | | Method | `getSpatialParametersAtTime` | `time`: double | None |
| | | Method | `getTimeline` | None | None |
| | | Method | `setName` | `name`: string | None |
| | | Method | `getName` | None | None |
| | | Method | `resetLayer` | None | None |
| | | Method | `getLayerJsonDescrip` | None | None |
| | | Method | `setLayerJsonDescrip` | `descrip`: string, `makeAllDominant`: bool | None |
| | | Method | `getJsonDescrip` | None | None |
| | | Method | `initFromJsonDescrip` | `descrip`: string | None |
| | | Method | `setOpacity` | `value`: double | None |
| | | Method | `getOpacity` | None | None |
| | | Method | `resetOpacity` | None | None |
| | | Method | `setVolume` | `value`: double | None |
| | | Method | `getVolume` | None | None |
| | | Method | `resetVolume` | None | None |
| | | Method | `muteLayer` | None | None |
| | | Method | `unMuteLayer` | None | None |
| | | Method | `getIsLayerMuted` | None | None |
| | | Method | `muteAudio` | None | None |
| | | Method | `unMuteAudio` | None | None |
| | | Method | `getIsAudioMuted` | None | None |
| | | Method | `getDmxMuteState` | None | None |
| | | Method | `setDmxMuteState` | `muteState`: uint | None |
| | | Method | `toggleExplicitMute` | `flag`: uint | None |
| | | Method | `setTransport` | `mode`: int, `loop`: bool | None |
| | | Method | `getTransportMode` | None | None |
| | | Method | `resetTransportMode` | None | None |
| | | Method | `getTransportLoop` | None | None |
| | | Method | `assignResource` | `id`: double | None |
| | | Method | `assignResourceWithFade` | `id`: double, `fadeDuration`: double | None |
| | | Method | `getAssignedResource` | None | None |
| | | Method | `resetAssignedResource` | None | None |
| | | Method | `getAssignedModelResource` | None | None |
| | | Method | `resetAssignedModelResource` | None | None |
| | | Method | `getFxNames` | None | None |
| | | Method | `setFadeDurationDominantResourceChange` | `value`: double | None |
| | | Method | `getFadeDurationDominantResourceChange` | None | None |
| | | Method | `createClip` | None | None |
| | | Method | `createClipAtTime` | `timeInFrames`: double | None |
| | | Method | `controlClipBorder` | `clip`: handle, `isEnter`: bool, `isIncremental`: bool, `entryTime`: double | None |
| | | Method | `getClipAtIndex` | `index`: int | None |
| | | Method | `getClips` | None | None |
| | | Method | `getClipCurrent` | `offset`: int | None |
| | | Method | `getClipsSelected` | None | None |
| | | Method | `removeClips` | None | None |
| | | Method | `setHomeScreenFromScreenName` | `screenName`: string | None |
| | | Method | `getHomeScreenName` | None | None |
| | | Method | `setBlendMode` | `blendMode`: string | None |
| | | Method | `getBlendMode` | None | None |
| | | Method | `addEffectById` | `id`: double | None |
| | | Method | `setPreloadPermanently` | `doPreloadPermanently`: bool | None |
| | | Method | `getPreloadPermanently` | None | None |
| | | Method | `setRestrictToServiceWithIps` | `doRestrict`: bool, `ipAdresses`: string[] | None |
| | | Method | `getRestrictToService` | None | None |
| | | Method | `getRestrictedServiceIps` | None | None |
| | | Method | `getOffsets` | None | None |
| | | Method | `setOffsets` | `x`: optional<double>, `y`: optional<double>, `z`: optional<double>, `xr`: optional<double>, `yr`: optional<double>, `zr`: optional<double>, `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | None |
| | | Method | `setCurrentValuesToOffset` | `typeIndex`: int, `resetDominant`: optional<bool>, `removeKeyframesClips`: optional<bool> | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Timelines | Class | | `Clip` | | |
| | | Method | `getId` | None | None |
| | | Method | `removeThis` | None | None |
| | | Method | `getTimeline` | None | None |
| | | Method | `setTime` | `time`: double | None |
| | | Method | `getTime` | None | None |
| | | Method | `setDuration` | `duration`: double | None |
| | | Method | `getDuration` | None | None |
| | | Method | `setLabel` | `label`: string | None |
| | | Method | `getLabel` | None | None |
| | | Method | `getPlayMode` | None | None |
| | | Method | `setPlayMode` | `playMode`: int | None |
| | | Method | `getSpeed` | None | None |
| | | Method | `setSpeed` | `speed`: double | None |
| | | Method | `getBlendFrames` | None | None |
| | | Method | `setBlendFrames` | `doFrameblending`: bool | None |
| | | Method | `getInpoint` | None | None |
| | | Method | `setInpoint` | `inpoint`: double | None |
| | | Method | `getOutpoint` | None | None |
| | | Method | `setOutpoint` | `inpoint`: double | None |
| | | Method | `assignResource` | `resId`: double, `setToResourceDuration`: optional<bool> | None |
| | | Method | `getAssignedResource` | None | None |
| | | Method | `setToResourceDuration` | None | None |
| | | Method | `createEvent` | `namePath`: string, `time`: double, `value`: double | None |
| | | Method | `createEventInPixelSpace` | `namePath`: string, `time`: double, `value`: double | None |
| | | Method | `removeEvent` | `namePath`: string, `time`: double | None |
| | | Method | `createPauseCueBeforeClip` | None | None |
| | | Method | `setColorTransformPath` | `colorTransformPath`: string | None |
| | | Method | `getColorTransformPath` | None | None |
| | | Method | `clearColorTransformPath` | None | None |
| | | Method | `getKeyframesAsJsonString` | None | None |
| Timelines | Class | | `Node` | | |
| | | Method | `getParameters` | None | None |
| | | Method | `getName` | None | None |
| | | Method | `getParamWithName` | `name`: string | None |
| | | Method | `setValues` | `values`: double[] | None |
| | | Method | `getValues` | None | None |
| | | Method | `resetValues` | None | None |
| | | Method | `storeValues` | None | None |
| | | Method | `mute` | None | None |
| | | Method | `unMute` | None | None |
| | | Method | `getIsMuted` | None | None |
| | | Method | `getTimeline` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Timelines | Class | | `Param` | | |
| | | Method | `getName` | None | None |
| | | Method | `getIsChannel` | None | None |
| | | Method | `setValue` | `value`: timelineParamValue | None |
| | | Method | `setValueRelativ` | `value`: double | None |
| | | Method | `getValue` | None | None |
| | | Method | `resetValue` | None | None |
| | | Method | `storeValue` | None | None |
| | | Method | `setTransportAttributes` | `mode`: int, `speed`: double, `loop`: bool, `inpoint`: int, `outpoint`: int | None |
| | | Method | `getAttributes` | None | None |
| | | Method | `mute` | None | None |
| | | Method | `unMute` | None | None |
| | | Method | `getIsMuted` | None | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Timelines | Class | | `Cue` | | |
| | | Method | `removeThis` | None | None |
| | | Method | `apply` | None | None |
| | | Method | `blendToThis` | `blendDurationInSeconds`: double | None |
| | | Method | `getAttributes` | None | None |
| | | Method | `getTimeline` | None | None |
| | | Method | `getIndex` | None | None |
| | | Method | `getName` | None | None |
| | | Method | `setName` | `name`: string | None |
| | | Method | `getNote` | None | None |
| | | Method | `setNote` | `note`: string | None |
| | | Method | `getOperation` | None | None |
| | | Method | `setOperation` | `operation`: int | None |
| | | Method | `getJumpMode` | None | None |
| | | Method | `setJumpMode` | `jumpMode`: int | None |
| | | Method | `getJumpGoalTime` | None | None |
| | | Method | `setJumpGoalTime` | `time`: double | None |
| | | Method | `getJumpGoalLabel` | None | None |
| | | Method | `getJumpGoalCue` | None | None |
| | | Method | `setJumpGoalLabel` | `jumpGoalLabel`: string | None |
| | | Method | `getNumber` | None | None |
| | | Method | `setNumber` | `number`: int | None |
| | | Method | `getWaitDuration` | None | None |
| | | Method | `setWaitDuration` | `time`: double | None |
| | | Method | `getBlendDuration` | None | None |
| | | Method | `setBlendDuration` | `timeInFrames`: double | None |
| | | Method | `getTime` | None | None |
| | | Method | `setTime` | `time`: double | None |
| | | Method | `getTimelineToTriggerName` | None | None |
| | | Method | `setTimelineToTrigger` | `nameTimeline`: string | None |
| | | Method | `getTimelineTriggerMode` | None | None |
| | | Method | `setTimelineTriggerMode` | `mode`: int | None |
| | | Method | `getTimelineTriggerApplyTime` | None | None |
| | | Method | `setTimelineTriggerApplyTime` | `time`: double | None |
| | | Method | `setTimelineTriggerApplyCue` | `goalCueLabel`: string | None |
| | | Method | `getCountdown` | None | None |
| | | Method | `getCountdownHMSF` | None | None |
| | | Method | `setCommand` | `conveyorName`: string, `commandData`: string | None |
| | | Method | `getInst` | `instancePath`: string | None |
| | | Method | `getHandleFromInstancePath` | `instancePath`: string | None |
| | | Method | `getInstancePath` | None | None |
| Calibration | Function | | `setMarkerPositions` | `positions`: double[], `markerIds`: int[] | None |
| WebViews | Function | | `loadDeviceUi` | `devicePath`: string | None |
| WebViews | Function | | `activatePreviousFunc` | None | None |
| WebViews | Function | | `activateNextFunc` | None | None |
| WebViews | Function | | `getLastActivatedFunc` | None | None |
| WebViews | Function | | `deviceActivated` | `devicePath`: string, `withSelection`: bool | None |
| WebViews | Function | | `funcActivated` | `funcPath`: string, `withSelection`: bool | None |
| WebViews | Function | | `setFuncBodyState` | `funcPath`: string, `state`: string | None |
| WebViews | Function | | `getFuncBodyState` | `funcPath`: string | None |
| WebViews | Function | | `setTag` | `tag`: string, `text`: string | None |
| WebViews | Function | | `setEditorIsUsingBlocks` | `useBlocks`: bool | None |
| Ui | Function | | `getComboBoxWithId` | `id`: double | None |
| Ui | Function | | `setAppMode` | `mode`: int | None |
| Ui | Function | | `getAppMode` | None | None |
| Ui | Function | | `getDisplayTestpattern` | None | None |
| Ui | Function | | `setDisplayTestpattern` | `display`: bool | None |
| Ui | Function | | `getPreviewCameraAsJsonString` | None | None |
| Ui | Function | | `setPreviewCameraAsJsonString` | `cameraFrustrumStateString`: string | None |
| Ui | Function | | `setDisableContentRendering` | `state`: bool | None |
| Ui | Function | | `getIsContentRenderingDisabled` | None | None |
| Ui | Function | | `setDisableWorkspaceRendering` | `state`: bool | None |
| Ui | Function | | `getIsWorkspaceRenderingDisabled` | None | None |
| Ui | Class | | `ComboBox` | | |
| | | Method | `clear` | None | None |
| | | Method | `addItem` | `item`: string, `id`: int | None |
| | | Method | `setSelectedId` | `id`: int | None |
| | | Method | `getSelectedId` | None | None |
| Direct | Function | | `setRegistered` | `hdls`: handle[], `expectedFrequency`: int, `dampingMs`: int, `usageHints`: string[] | None |
| Direct | Function | | `reloadRegistered` | None | None |
| Direct | Function | | `registerScreen` | `name`: string, `expectedFrequency`: int, `dampingMs`: int | None |
| Direct | Function | | `registerParam` | `instancePath`: string | None |
| Direct | Function | | `registerCamera` | `cameraName`: string, `expectedFrequency`: int | None |
| Direct | Function | | `registerPerspective` | `screenName`: string, `expectedFrequency`: int | None |
| Direct | Class | | `Screen` | | |
| | | Method | `setPosition` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double> | None |
| | | Method | `setRotation` | `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `setPosRot` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double> | None |
| | | Method | `setPosRotScale` | `xPos`: optional<double>, `yPos`: optional<double>, `zPos`: optional<double>, `xRot`: optional<double>, `yRot`: optional<double>, `zRot`: optional<double>, `xScale`: optional<double>, `yScale`: optional<double>, `zScale`: optional<double> | None |
| | | Method | `enableLogging` | `enable`: bool | None |
| Direct | Class | | `Param` | | |
| | | Method | `setValue` | `value`: double | None |
| | | Method | `enableLogging` | `enable`: bool | None |
| Direct | Class | | `Camera` | | |
| | | Method | `setPosition` | `xPos`: double, `yPos`: double, `zPos`: double | None |
| | | Method | `setRotation` | `xRot`: double, `yRot`: double, `zRot`: double | None |
| | | Method | `setTransformation` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double | None |
| | | Method | `setTransformationAndLensProps` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `iris`: double, `k1`: double, `k2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double | None |
| | | Method | `setTransformationAndLensPropsExt` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `focalDistance`: double, `zoom`: double, `iris`: double, `k1`: double, `k2`: double, `k3`: double, `p1`: double, `p2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double, `overscan`: double | None |
| Direct | Class | | `Perspective` | | |
| | | Method | `setTransformation` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double | None |
| | | Method | `setTransformationAndLensProps` | `xPos`: double, `yPos`: double, `zPos`: double, `xRot`: double, `yRot`: double, `zRot`: double, `fov`: double, `aspectRatio`: double, `nearClip`: double, `farClip`: double, `aperture`: double, `focus`: double, `iris`: double, `k1`: double, `k2`: double, `centerX`: double, `centerY`: double, `panelWidth`: double | None |
