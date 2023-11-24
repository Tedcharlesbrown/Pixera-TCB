def getApiRevision() -> int:
    method = "Pixera.Utility.getApiRevision"
    params = [""]

    return [method,params,[]]

def getHasFunction(functionName: str) -> bool:
    method = "Pixera.Utility.getHasFunction"
    params = ["functionName"]

    return [method,params,[functionName]]

def outputDebug(message: str) -> str:
    method = "Pixera.Utility.outputDebug"
    params = ["message"]

    return [method,params,[message]]

def getLicenseJson() -> str:
    method = "Pixera.Utility.getLicenseJson"
    params = [""]

    return [method,params,[]]

def getCurrentTime() -> float:
    method = "Pixera.Utility.getCurrentTime"
    params = [""]

    return [method,params,[]]

def getCurrentTimeAsString() -> str:
    method = "Pixera.Utility.getCurrentTimeAsString"
    params = [""]

    return [method,params,[]]

def noop() -> None:
    method = "Pixera.Utility.noop"
    params = [""]

    return [method,params,[]]

def requestCallback(functionName: str) -> None:
    method = "Pixera.Utility.requestCallback"
    params = ["functionName"]

    return [method,params,[functionName]]

def readFileString(path: str) -> str:
    method = "Pixera.Utility.readFileString"
    params = ["path"]

    return [method,params,[path]]

def writeFileString(path: str, fileStr: str) -> None:
    method = "Pixera.Utility.writeFileString"
    params = ["path, fileStr"]

    return [method,params,[path, fileStr]]

def getAccessRecipe(hdlPath: str) -> str:
    method = "Pixera.Utility.getAccessRecipe"
    params = ["hdlPath"]

    return [method,params,[hdlPath]]

def pollMonitoring() -> str:
    method = "Pixera.Utility.pollMonitoring"
    params = [""]

    return [method,params,[]]

def unsubscribeMonitoringSubject(subject: str) -> bool:
    method = "Pixera.Utility.unsubscribeMonitoringSubject"
    params = ["subject"]

    return [method,params,[subject]]

def subscribeMonitoringSubject(subject: str) -> bool:
    method = "Pixera.Utility.subscribeMonitoringSubject"
    params = ["subject"]

    return [method,params,[subject]]

def setMonitoringEventMode(mode: str) -> bool:
    method = "Pixera.Utility.setMonitoringEventMode"
    params = ["mode"]

    return [method,params,[mode]]

def monitoringEvent(eventDescription: str) -> None:
    method = "Pixera.Utility.monitoringEvent"
    params = ["eventDescription"]

    return [method,params,[eventDescription]]

def setShowContextInReplies(doShow: bool) -> bool:
    method = "Pixera.Utility.setShowContextInReplies"
    params = ["doShow"]

    return [method,params,[doShow]]

def setMonitoringHasDelimiter(hasDelimiter: bool) -> bool:
    method = "Pixera.Utility.setMonitoringHasDelimiter"
    params = ["hasDelimiter"]

    return [method,params,[hasDelimiter]]

def runJsScript(jsFunction: str, jsCode: str) -> str:
    method = "Pixera.Utility.runJsScript"
    params = ["jsFunction, jsCode"]

    return [method,params,[jsFunction, jsCode]]

def dynamicRebuildFromJsonDescription(deviceName: str, jsonDescription: str, folder: str) -> None:
    method = "Pixera.Utility.dynamicRebuildFromJsonDescription"
    params = ["deviceName, jsonDescription, folder"]

    return [method,params,[deviceName, jsonDescription, folder]]

def getConveyor(conveyorName: str) -> handle:
    method = "Pixera.Network.getConveyor"
    params = ["conveyorName"]

    return [method,params,[conveyorName]]

class Conveyor:
    def sendString(str: str) -> None:
        method = "Pixera.Network.Conveyor.sendString"
        params = ["str"]

def setTransportModeOnTimelineAtIndex(index: int, mode: int) -> bool:
    method = "Pixera.Compound.setTransportModeOnTimelineAtIndex"
    params = ["index, mode"]

    return [method,params,[index, mode]]

def setTransportModeOnTimeline(timelineName: str, mode: int) -> None:
    method = "Pixera.Compound.setTransportModeOnTimeline"
    params = ["timelineName, mode"]

    return [method,params,[timelineName, mode]]

def toggleTransport(timelineName: str) -> None:
    method = "Pixera.Compound.toggleTransport"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def getTransportModeOnTimeline(timelineName: str) -> int:
    method = "Pixera.Compound.getTransportModeOnTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def setOpacityOnTimeline(timelineName: str, opacity: float) -> None:
    method = "Pixera.Compound.setOpacityOnTimeline"
    params = ["timelineName, opacity"]

    return [method,params,[timelineName, opacity]]

def getOpacityOnTimeline(timelineName: str) -> float:
    method = "Pixera.Compound.getOpacityOnTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def startFirstTimeline() -> None:
    method = "Pixera.Compound.startFirstTimeline"
    params = [""]

    return [method,params,[]]

def pauseFirstTimeline() -> None:
    method = "Pixera.Compound.pauseFirstTimeline"
    params = [""]

    return [method,params,[]]

def stopFirstTimeline() -> None:
    method = "Pixera.Compound.stopFirstTimeline"
    params = [""]

    return [method,params,[]]

def setPosValue(val: float) -> None:
    method = "Pixera.Compound.setPosValue"
    params = ["val"]

    return [method,params,[val]]

def setPosValueXY(valX: float, valY: float) -> None:
    method = "Pixera.Compound.setPosValueXY"
    params = ["valX, valY"]

    return [method,params,[valX, valY]]

def setParamValue(path: str, value: float) -> None:
    method = "Pixera.Compound.setParamValue"
    params = ["path, value"]

    return [method,params,[path, value]]

def applyCueAtIndexOnTimelineAtIndex(cueIndex: int, timelineIndex: int) -> None:
    method = "Pixera.Compound.applyCueAtIndexOnTimelineAtIndex"
    params = ["cueIndex, timelineIndex"]

    return [method,params,[cueIndex, timelineIndex]]

def applyCueNumberOnTimelineAtIndex(cueNumber: int, timelineIndex: int) -> None:
    method = "Pixera.Compound.applyCueNumberOnTimelineAtIndex"
    params = ["cueNumber, timelineIndex"]

    return [method,params,[cueNumber, timelineIndex]]

def applyCueNumberOnTimeline(timelineName: str, cueNumber: int) -> None:
    method = "Pixera.Compound.applyCueNumberOnTimeline"
    params = ["timelineName, cueNumber"]

    return [method,params,[timelineName, cueNumber]]

def applyCueOnTimeline(timelineName: str, cueName: str) -> None:
    method = "Pixera.Compound.applyCueOnTimeline"
    params = ["timelineName, cueName"]

    return [method,params,[timelineName, cueName]]

def addResourceToFolder(namePath: str, filePath: str) -> handle:
    method = "Pixera.Compound.addResourceToFolder"
    params = ["namePath, filePath"]

    return [method,params,[namePath, filePath]]

def assignResourceToLayer(resourcePath: str, layerPath: str) -> None:
    method = "Pixera.Compound.assignResourceToLayer"
    params = ["resourcePath, layerPath"]

    return [method,params,[resourcePath, layerPath]]

def refreshResource(resourcePath: str) -> None:
    method = "Pixera.Compound.refreshResource"
    params = ["resourcePath"]

    return [method,params,[resourcePath]]

def setTransportModeOnLayer(layerPath: str, mode: int, loop: bool) -> None:
    method = "Pixera.Compound.setTransportModeOnLayer"
    params = ["layerPath, mode, loop"]

    return [method,params,[layerPath, mode, loop]]

def getTransportModeOnLayer(layerPath: str) -> int:
    method = "Pixera.Compound.getTransportModeOnLayer"
    params = ["layerPath"]

    return [method,params,[layerPath]]

def getResourceAssignedToLayer(layerPath: str) -> str:
    method = "Pixera.Compound.getResourceAssignedToLayer"
    params = ["layerPath"]

    return [method,params,[layerPath]]

def assignResourceToClipAtTimeByDmxId(layerPath: str, dmxFolderId: int, dmxFileId: int, time: float) -> None:
    method = "Pixera.Compound.assignResourceToClipAtTimeByDmxId"
    params = ["layerPath, dmxFolderId, dmxFileId, time"]

    return [method,params,[layerPath, dmxFolderId, dmxFileId, time]]

def assignResourceToClipAtHMSFStringByDmxId(layerPath: str, dmxFolderId: int, dmxFileId: int, hmsf: str) -> None:
    method = "Pixera.Compound.assignResourceToClipAtHMSFStringByDmxId"
    params = ["layerPath, dmxFolderId, dmxFileId, hmsf"]

    return [method,params,[layerPath, dmxFolderId, dmxFileId, hmsf]]

def assignResourceToClipAtHMSFByDmxId(layerPath: str, dmxFolderId: int, dmxFileId: int, h: int, m: int, s: int, f: int) -> None:
    method = "Pixera.Compound.assignResourceToClipAtHMSFByDmxId"
    params = ["layerPath, dmxFolderId, dmxFileId, h, m, s, f"]

    return [method,params,[layerPath, dmxFolderId, dmxFileId, h, m, s, f]]

def setCurrentTimeOfTimeline(timelineName: str, time: int) -> None:
    method = "Pixera.Compound.setCurrentTimeOfTimeline"
    params = ["timelineName, time"]

    return [method,params,[timelineName, time]]

def setCurrentTimeOfTimelineInSeconds(timelineName: str, time: float) -> None:
    method = "Pixera.Compound.setCurrentTimeOfTimelineInSeconds"
    params = ["timelineName, time"]

    return [method,params,[timelineName, time]]

def setCurrentTimeAndTransportModeOfTimelineInSeconds(timelineName: str, time: float, mode: int) -> None:
    method = "Pixera.Compound.setCurrentTimeAndTransportModeOfTimelineInSeconds"
    params = ["timelineName, time, mode"]

    return [method,params,[timelineName, time, mode]]

def getFpsOfTimeline(timelineName: str) -> float:
    method = "Pixera.Compound.getFpsOfTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def getCurrentTimeOfTimeline(timelineName: str) -> int:
    method = "Pixera.Compound.getCurrentTimeOfTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def getCurrentTimeOfTimelineInSeconds(timelineName: str) -> float:
    method = "Pixera.Compound.getCurrentTimeOfTimelineInSeconds"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def getCurrentHMSFOfTimeline(timelineName: str) -> str:
    method = "Pixera.Compound.getCurrentHMSFOfTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def getCurrentCountdownOfTimeline(timelineName: str) -> int:
    method = "Pixera.Compound.getCurrentCountdownOfTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def getCurrentCountdownHMSFOfTimeline(timelineName: str) -> str:
    method = "Pixera.Compound.getCurrentCountdownHMSFOfTimeline"
    params = ["timelineName"]

    return [method,params,[timelineName]]

def startOpacityAnimationOfTimeline(timelineName: str, fadeIn: bool, fullFadeDuration: float) -> None:
    method = "Pixera.Compound.startOpacityAnimationOfTimeline"
    params = ["timelineName, fadeIn, fullFadeDuration"]

    return [method,params,[timelineName, fadeIn, fullFadeDuration]]

def createClipOnLayerAtTimeWithResource(layerPath: str, time: float, resourcePath: str) -> None:
    method = "Pixera.Compound.createClipOnLayerAtTimeWithResource"
    params = ["layerPath, time, resourcePath"]

    return [method,params,[layerPath, time, resourcePath]]

def removeClipOnLayerWithIndex(layerPath: str, clipIndex: int) -> None:
    method = "Pixera.Compound.removeClipOnLayerWithIndex"
    params = ["layerPath, clipIndex"]

    return [method,params,[layerPath, clipIndex]]

def removeAllClipsOnLayer(layerPath: str) -> None:
    method = "Pixera.Compound.removeAllClipsOnLayer"
    params = ["layerPath"]

    return [method,params,[layerPath]]

def getClipDurationInSecondsWithIndex(layerPath: str, clipIndex: int) -> float:
    method = "Pixera.Compound.getClipDurationInSecondsWithIndex"
    params = ["layerPath, clipIndex"]

    return [method,params,[layerPath, clipIndex]]

def getClipDurationInFramesWithIndex(layerPath: str, clipIndex: int) -> int:
    method = "Pixera.Compound.getClipDurationInFramesWithIndex"
    params = ["layerPath, clipIndex"]

    return [method,params,[layerPath, clipIndex]]

def getClipTimeInSecondsWithIndex(layerPath: str, clipIndex: int) -> float:
    method = "Pixera.Compound.getClipTimeInSecondsWithIndex"
    params = ["layerPath, clipIndex"]

    return [method,params,[layerPath, clipIndex]]

def getClipEndTimeInSecondsWithIndex(layerPath: str, clipIndex: int) -> float:
    method = "Pixera.Compound.getClipEndTimeInSecondsWithIndex"
    params = ["layerPath, clipIndex"]

    return [method,params,[layerPath, clipIndex]]

def getResourceDurationInSeconds(resourcePath: str) -> float:
    method = "Pixera.Compound.getResourceDurationInSeconds"
    params = ["resourcePath"]

    return [method,params,[resourcePath]]

def getParamValue(path: str) -> float:
    method = "Pixera.Compound.getParamValue"
    params = ["path"]

    return [method,params,[path]]

def setTimecodeInput(hour: int, minute: int, second: int, frame: int, elapsedTime: float, running: bool, freshMode: int, stateToken: int, format: int) -> float:
    method = "Pixera.Compound.setTimecodeInput"
    params = ["hour, minute, second, frame, elapsedTime, running, freshMode, stateToken, format"]

    return [method,params,[hour, minute, second, frame, elapsedTime, running, freshMode, stateToken, format]]

def takeOverAllClients() -> None:
    method = "Pixera.Compound.takeOverAllClients"
    params = [""]

    return [method,params,[]]

def setPauseSmpteInput(doPause: bool) -> None:
    method = "Pixera.Compound.setPauseSmpteInput"
    params = ["doPause"]

    return [method,params,[doPause]]

def closeApp(saveProject: bool) -> None:
    method = "Pixera.Session.closeApp"
    params = ["saveProject"]

    return [method,params,[saveProject]]

def loadProject(path: str) -> None:
    method = "Pixera.Session.loadProject"
    params = ["path"]

    return [method,params,[path]]

def saveProject() -> None:
    method = "Pixera.Session.saveProject"
    params = [""]

    return [method,params,[]]

def saveProjectAs(path: str) -> None:
    method = "Pixera.Session.saveProjectAs"
    params = ["path"]

    return [method,params,[path]]

def getProjectName() -> str:
    method = "Pixera.Session.getProjectName"
    params = [""]

    return [method,params,[]]

def setProjectName(name: str) -> None:
    method = "Pixera.Session.setProjectName"
    params = ["name"]

    return [method,params,[name]]

def getProjectDirectory() -> str:
    method = "Pixera.Session.getProjectDirectory"
    params = [""]

    return [method,params,[]]

def getControlMultiUserSessionName() -> str:
    method = "Pixera.Session.getControlMultiUserSessionName"
    params = [""]

    return [method,params,[]]

def shutdownSystem(mode: optional<int>) -> None:
    method = "Pixera.Session.shutdownSystem"
    params = ["mode"]

    return [method,params,[mode]]

def getLiveSystemIps() -> str[]:
    method = "Pixera.Session.getLiveSystemIps"
    params = [""]

    return [method,params,[]]

def getLiveSystemState(ip: str) -> str:
    method = "Pixera.Session.getLiveSystemState"
    params = ["ip"]

    return [method,params,[ip]]

def liveSystemStateChange(ip: str, state: str) -> None:
    method = "Pixera.Session.liveSystemStateChange"
    params = ["ip, state"]

    return [method,params,[ip, state]]

def shutdownLiveSystem(ip: str, mode: optional<int>) -> None:
    method = "Pixera.Session.shutdownLiveSystem"
    params = ["ip, mode"]

    return [method,params,[ip, mode]]

def wakeLiveSystem(ip: str) -> str:
    method = "Pixera.Session.wakeLiveSystem"
    params = ["ip"]

    return [method,params,[ip]]

def getLiveSystemMacAddress(ip: str) -> str:
    method = "Pixera.Session.getLiveSystemMacAddress"
    params = ["ip"]

    return [method,params,[ip]]

def startLiveSystem(ip: str) -> None:
    method = "Pixera.Session.startLiveSystem"
    params = ["ip"]

    return [method,params,[ip]]

def startLiveSystems() -> None:
    method = "Pixera.Session.startLiveSystems"
    params = [""]

    return [method,params,[]]

def stopLiveSystem(ip: str) -> None:
    method = "Pixera.Session.stopLiveSystem"
    params = ["ip"]

    return [method,params,[ip]]

def stopLiveSystems() -> None:
    method = "Pixera.Session.stopLiveSystems"
    params = [""]

    return [method,params,[]]

def restartLiveSystem(ip: str) -> None:
    method = "Pixera.Session.restartLiveSystem"
    params = ["ip"]

    return [method,params,[ip]]

def restartLiveSystems() -> None:
    method = "Pixera.Session.restartLiveSystems"
    params = [""]

    return [method,params,[]]

def remoteSystemStateChange(ip: str, state: str) -> None:
    method = "Pixera.Session.remoteSystemStateChange"
    params = ["ip, state"]

    return [method,params,[ip, state]]

def getRemoteSystemIps() -> str[]:
    method = "Pixera.Session.getRemoteSystemIps"
    params = [""]

    return [method,params,[]]

def getRemoteSystemState(ip: str) -> str:
    method = "Pixera.Session.getRemoteSystemState"
    params = ["ip"]

    return [method,params,[ip]]

def setVideoStreamActiveState(ip: str, device: str, isActive: bool) -> None:
    method = "Pixera.Session.setVideoStreamActiveState"
    params = ["ip, device, isActive"]

    return [method,params,[ip, device, isActive]]

def getVideoStreamActiveState(ip: str, device: str) -> bool:
    method = "Pixera.Session.getVideoStreamActiveState"
    params = ["ip, device"]

    return [method,params,[ip, device]]

def getDefaultClipDurationsAsJsonString() -> str:
    method = "Pixera.Session.getDefaultClipDurationsAsJsonString"
    params = [""]

    return [method,params,[]]

def getLiveSystems() -> handle[]:
    method = "Pixera.LiveSystems.getLiveSystems"
    params = [""]

    return [method,params,[]]

def liveSystemNotAvailable(reason: int, system: handle) -> None:
    method = "Pixera.LiveSystems.liveSystemNotAvailable"
    params = ["reason, system"]

    return [method,params,[reason, system]]

def getMultiUserMembers() -> handle[]:
    method = "Pixera.LiveSystems.getMultiUserMembers"
    params = [""]

    return [method,params,[]]

class MultiUserMember:
    def getName() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getName"
        params = [""]

    def getIp() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getIp"
        params = [""]

    def getState() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getState"
        params = [""]

    def getPerformanceMonitoringValuesJson() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getPerformanceMonitoringValuesJson"
        params = [""]

    def getPerformanceMonitoringValuesJsonEx(filter: str) -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getPerformanceMonitoringValuesJsonEx"
        params = ["filter"]

    def resetCumulativePerformanceMonitoringValues() -> None:
        method = "Pixera.LiveSystems.MultiUserMember.resetCumulativePerformanceMonitoringValues"
        params = [""]

    def ensureFileDistribution(includeNotUsedYet: bool) -> None:
        method = "Pixera.LiveSystems.MultiUserMember.ensureFileDistribution"
        params = ["includeNotUsedYet"]

    def shutDown(mode: int) -> None:
        method = "Pixera.LiveSystems.MultiUserMember.shutDown"
        params = ["mode"]

    def wakeUp() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.wakeUp"
        params = [""]

    def getMacAddress() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getMacAddress"
        params = [""]

    def resetEngine() -> None:
        method = "Pixera.LiveSystems.MultiUserMember.resetEngine"
        params = [""]

    def restartEngine() -> None:
        method = "Pixera.LiveSystems.MultiUserMember.restartEngine"
        params = [""]

    def startEngine() -> None:
        method = "Pixera.LiveSystems.MultiUserMember.startEngine"
        params = [""]

    def closeEngine() -> None:
        method = "Pixera.LiveSystems.MultiUserMember.closeEngine"
        params = [""]

    def triggerBackup(applyControlCommand: optional<bool>) -> None:
        method = "Pixera.LiveSystems.MultiUserMember.triggerBackup"
        params = ["applyControlCommand"]

    def getStructureJson() -> str:
        method = "Pixera.LiveSystems.MultiUserMember.getStructureJson"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.LiveSystems.MultiUserMember.getInst"
        params = ["instancePath"]

class LiveSystem:
    def getName() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getName"
        params = [""]

    def getIp() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getIp"
        params = [""]

    def getState() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getState"
        params = [""]

    def setBackupRole(role: int) -> None:
        method = "Pixera.LiveSystems.LiveSystem.setBackupRole"
        params = ["role"]

    def getBackupRole() -> int:
        method = "Pixera.LiveSystems.LiveSystem.getBackupRole"
        params = [""]

    def getPerformanceMonitoringValuesJson() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getPerformanceMonitoringValuesJson"
        params = [""]

    def getPerformanceMonitoringValuesJsonEx(filter: str) -> str:
        method = "Pixera.LiveSystems.LiveSystem.getPerformanceMonitoringValuesJsonEx"
        params = ["filter"]

    def resetCumulativePerformanceMonitoringValues() -> None:
        method = "Pixera.LiveSystems.LiveSystem.resetCumulativePerformanceMonitoringValues"
        params = [""]

    def moveMappingsToOutputs(hdlSrc: handle, outputIdPathMapStr: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.moveMappingsToOutputs"
        params = ["hdlSrc, outputIdPathMapStr"]

    def clearExportedMappings(path: str, onlyServicePath: bool) -> None:
        method = "Pixera.LiveSystems.LiveSystem.clearExportedMappings"
        params = ["path, onlyServicePath"]

    def exportMappings(path: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.exportMappings"
        params = ["path"]

    def importMappings(path: str, outputIdPathMapStr: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.importMappings"
        params = ["path, outputIdPathMapStr"]

    def exportMappingsDirectly(path: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.exportMappingsDirectly"
        params = ["path"]

    def importMappingsDirectly(path: str, outputIdPathMapStr: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.importMappingsDirectly"
        params = ["path, outputIdPathMapStr"]

    def exportMappingsToLiveSystemPath(parentPath: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.exportMappingsToLiveSystemPath"
        params = ["parentPath"]

    def importMappingsFromLiveSystemPath(parentPath: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.importMappingsFromLiveSystemPath"
        params = ["parentPath"]

    def clearExportedMappingsAtLiveSystemPath(path: str) -> None:
        method = "Pixera.LiveSystems.LiveSystem.clearExportedMappingsAtLiveSystemPath"
        params = ["path"]

    def ensureFileDistribution(includeNotUsedYet: bool) -> None:
        method = "Pixera.LiveSystems.LiveSystem.ensureFileDistribution"
        params = ["includeNotUsedYet"]

    def shutDown(mode: int) -> None:
        method = "Pixera.LiveSystems.LiveSystem.shutDown"
        params = ["mode"]

    def wakeUp() -> str:
        method = "Pixera.LiveSystems.LiveSystem.wakeUp"
        params = [""]

    def getMacAddress() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getMacAddress"
        params = [""]

    def getGraphicsDevices() -> handle[]:
        method = "Pixera.LiveSystems.LiveSystem.getGraphicsDevices"
        params = [""]

    def getEnabledOutputs() -> handle[]:
        method = "Pixera.LiveSystems.LiveSystem.getEnabledOutputs"
        params = [""]

    def getAllOutputs() -> handle[]:
        method = "Pixera.LiveSystems.LiveSystem.getAllOutputs"
        params = [""]

    def getVideoStreamOutputs() -> handle[]:
        method = "Pixera.LiveSystems.LiveSystem.getVideoStreamOutputs"
        params = [""]

    def resetEngine() -> None:
        method = "Pixera.LiveSystems.LiveSystem.resetEngine"
        params = [""]

    def restartEngine() -> None:
        method = "Pixera.LiveSystems.LiveSystem.restartEngine"
        params = [""]

    def startEngine() -> None:
        method = "Pixera.LiveSystems.LiveSystem.startEngine"
        params = [""]

    def closeEngine() -> None:
        method = "Pixera.LiveSystems.LiveSystem.closeEngine"
        params = [""]

    def setAudioMasterVolume(channel: int, volume: float) -> None:
        method = "Pixera.LiveSystems.LiveSystem.setAudioMasterVolume"
        params = ["channel, volume"]

    def getAudioMasterVolume(channel: int) -> float:
        method = "Pixera.LiveSystems.LiveSystem.getAudioMasterVolume"
        params = ["channel"]

    def setAudioMasterMute(channel: int, state: bool) -> None:
        method = "Pixera.LiveSystems.LiveSystem.setAudioMasterMute"
        params = ["channel, state"]

    def getAudioMasterMute(channel: int) -> bool:
        method = "Pixera.LiveSystems.LiveSystem.getAudioMasterMute"
        params = ["channel"]

    def setAudioTimecodeInput(channel: int, state: bool) -> None:
        method = "Pixera.LiveSystems.LiveSystem.setAudioTimecodeInput"
        params = ["channel, state"]

    def triggerBackup(applyControlCommand: optional<bool>) -> None:
        method = "Pixera.LiveSystems.LiveSystem.triggerBackup"
        params = ["applyControlCommand"]

    def getStructureJson() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getStructureJson"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.LiveSystems.LiveSystem.getInst"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.LiveSystems.LiveSystem.getInstancePath"
        params = [""]

class GraphicsDevice:
    def getName() -> str:
        method = "Pixera.LiveSystems.GraphicsDevice.getName"
        params = [""]

    def getEnabledOutputs() -> handle[]:
        method = "Pixera.LiveSystems.GraphicsDevice.getEnabledOutputs"
        params = [""]

    def getAllOutputs() -> handle[]:
        method = "Pixera.LiveSystems.GraphicsDevice.getAllOutputs"
        params = [""]

class Output:
    def getName() -> str:
        method = "Pixera.LiveSystems.Output.getName"
        params = [""]

    def setActive(active: bool) -> None:
        method = "Pixera.LiveSystems.Output.setActive"
        params = ["active"]

    def getActive() -> bool:
        method = "Pixera.LiveSystems.Output.getActive"
        params = [""]

    def setIdentify(state: bool) -> None:
        method = "Pixera.LiveSystems.Output.setIdentify"
        params = ["state"]

    def getIdentify() -> bool:
        method = "Pixera.LiveSystems.Output.getIdentify"
        params = [""]

    def getAssignedScreens() -> handle[]:
        method = "Pixera.LiveSystems.Output.getAssignedScreens"
        params = [""]

    def getAssignedProjectors() -> handle[]:
        method = "Pixera.LiveSystems.Output.getAssignedProjectors"
        params = [""]

    def getEnabled() -> bool:
        method = "Pixera.LiveSystems.Output.getEnabled"
        params = [""]

    def getForPreview() -> bool:
        method = "Pixera.LiveSystems.Output.getForPreview"
        params = [""]

class VideoStream:
    def getName() -> str:
        method = "Pixera.LiveSystems.VideoStream.getName"
        params = [""]

    def setActive(active: bool) -> None:
        method = "Pixera.LiveSystems.VideoStream.setActive"
        params = ["active"]

    def getActive() -> bool:
        method = "Pixera.LiveSystems.VideoStream.getActive"
        params = [""]

def getShowDimsInPixels() -> bool:
    method = "Pixera.Settings.SettingsGeneral.getShowDimsInPixels"
    params = [""]

    return [method,params,[]]

def getShowScaleAsSize() -> bool:
    method = "Pixera.Settings.SettingsGeneral.getShowScaleAsSize"
    params = [""]

    return [method,params,[]]

def setFadeToTimeDelay(timeInMilliseconds: int) -> None:
    method = "Pixera.Settings.SettingsGeneral.setFadeToTimeDelay"
    params = ["timeInMilliseconds"]

    return [method,params,[timeInMilliseconds]]

def getFadeToTimeDelay() -> int:
    method = "Pixera.Settings.SettingsGeneral.getFadeToTimeDelay"
    params = [""]

    return [method,params,[]]

def getTranscodingPresets() -> str[]:
    method = "Pixera.Settings.SettingsTranscoding.getTranscodingPresets"
    params = [""]

    return [method,params,[]]

def addOrChangeTranscodingPreset(preset: str) -> None:
    method = "Pixera.Settings.SettingsTranscoding.addOrChangeTranscodingPreset"
    params = ["preset"]

    return [method,params,[preset]]

def getScreenWithName(name: str) -> handle:
    method = "Pixera.Screens.getScreenWithName"
    params = ["name"]

    return [method,params,[name]]

def setNamedScreenPosition(name: str, xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> None:
    method = "Pixera.Screens.setNamedScreenPosition"
    params = ["name, xPos, yPos, zPos"]

    return [method,params,[name, xPos, yPos, zPos]]

def getScreens() -> handle[]:
    method = "Pixera.Screens.getScreens"
    params = [""]

    return [method,params,[]]

def getScreenNames() -> str[]:
    method = "Pixera.Screens.getScreenNames"
    params = [""]

    return [method,params,[]]

def getFirstTimelineWithHomeScreen(screenName: str) -> handle:
    method = "Pixera.Screens.getFirstTimelineWithHomeScreen"
    params = ["screenName"]

    return [method,params,[screenName]]

def getStudioCameras() -> handle[]:
    method = "Pixera.Screens.getStudioCameras"
    params = [""]

    return [method,params,[]]

class Screen:
    def getId() -> float:
        method = "Pixera.Screens.Screen.getId"
        params = [""]

    def getName() -> str:
        method = "Pixera.Screens.Screen.getName"
        params = [""]

    def setPosition(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setPosition"
        params = ["xPos, yPos, zPos"]

    def getPosition() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getPosition"
        params = [""]

    def setRotation(xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setRotation"
        params = ["xRot, yRot, zRot"]

    def getRotation() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getRotation"
        params = [""]

    def setScale(xScale: optional<float>, yScale: optional<float>, zScale: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setScale"
        params = ["xScale, yScale, zScale"]

    def getScale() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getScale"
        params = [""]

    def setPosRot(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>, xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setPosRot"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot"]

    def setPosRotScale(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>, xRot: optional<float>, yRot: optional<float>, zRot: optional<float>, xScale: optional<float>, yScale: optional<float>, zScale: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setPosRotScale"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, xScale, yScale, zScale"]

    def getPersepective() -> handle:
        method = "Pixera.Screens.Screen.getPersepective"
        params = [""]

    def snapPerspectiveCornersToScreen(mode: int) -> None:
        method = "Pixera.Screens.Screen.snapPerspectiveCornersToScreen"
        params = ["mode"]

    def setPerspectivePosition(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setPerspectivePosition"
        params = ["xPos, yPos, zPos"]

    def setPerspectivePositionWithLookAt(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setPerspectivePositionWithLookAt"
        params = ["xPos, yPos, zPos"]

    def getPerspectivePosition() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getPerspectivePosition"
        params = [""]

    def setPerspectiveRotation(xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setPerspectiveRotation"
        params = ["xRot, yRot, zRot"]

    def getPerspectiveRotation() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getPerspectiveRotation"
        params = [""]

    def setCameraPosition(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setCameraPosition"
        params = ["xPos, yPos, zPos"]

    def setCameraPositionWithLookAt(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setCameraPositionWithLookAt"
        params = ["xPos, yPos, zPos"]

    def getCameraPosition() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getCameraPosition"
        params = [""]

    def setCameraRotation(xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> bool:
        method = "Pixera.Screens.Screen.setCameraRotation"
        params = ["xRot, yRot, zRot"]

    def getCameraRotation() -> ScreenPosValues:
        method = "Pixera.Screens.Screen.getCameraRotation"
        params = [""]

    def setContentSamplingFrustumBase(x: float, y: float, width: float, height: float, rotation: float, originScreenId: float) -> None:
        method = "Pixera.Screens.Screen.setContentSamplingFrustumBase"
        params = ["x, y, width, height, rotation, originScreenId"]

    def runCalibration(mode: str, diff: str) -> None:
        method = "Pixera.Screens.Screen.runCalibration"
        params = ["mode, diff"]

    def editCalibration(diff: str) -> None:
        method = "Pixera.Screens.Screen.editCalibration"
        params = ["diff"]

    def resetWarpFile(diff: str) -> None:
        method = "Pixera.Screens.Screen.resetWarpFile"
        params = ["diff"]

    def loadWarpFile(filePath: str) -> None:
        method = "Pixera.Screens.Screen.loadWarpFile"
        params = ["filePath"]

    def loadWarpFileWithDiff(filePath: str, diff: str) -> None:
        method = "Pixera.Screens.Screen.loadWarpFileWithDiff"
        params = ["filePath, diff"]

    def addWarpFile(filePath: str) -> None:
        method = "Pixera.Screens.Screen.addWarpFile"
        params = ["filePath"]

    def addWarpFileWithDiff(filePath: str, diff: str) -> None:
        method = "Pixera.Screens.Screen.addWarpFileWithDiff"
        params = ["filePath, diff"]

    def loadColorCalibration(calibrationName: str) -> None:
        method = "Pixera.Screens.Screen.loadColorCalibration"
        params = ["calibrationName"]

    def runColorCalibration() -> None:
        method = "Pixera.Screens.Screen.runColorCalibration"
        params = [""]

    def setIsVisible(isVisible: bool) -> None:
        method = "Pixera.Screens.Screen.setIsVisible"
        params = ["isVisible"]

    def getIsVisible() -> bool:
        method = "Pixera.Screens.Screen.getIsVisible"
        params = [""]

    def setIsProjectable(isProjectable: bool) -> None:
        method = "Pixera.Screens.Screen.setIsProjectable"
        params = ["isProjectable"]

    def getIsProjectable() -> bool:
        method = "Pixera.Screens.Screen.getIsProjectable"
        params = [""]

    def triggerRefreshMapping() -> None:
        method = "Pixera.Screens.Screen.triggerRefreshMapping"
        params = [""]

    def resetAllColorCorrections() -> None:
        method = "Pixera.Screens.Screen.resetAllColorCorrections"
        params = [""]

    def setColorCorrectionWithPath(path: str, value: float) -> None:
        method = "Pixera.Screens.Screen.setColorCorrectionWithPath"
        params = ["path, value"]

    def getColorCorrectionWithPath(path: str) -> float:
        method = "Pixera.Screens.Screen.getColorCorrectionWithPath"
        params = ["path"]

    def setColorCorrectionAsJsonString(colorCorrection: str) -> None:
        method = "Pixera.Screens.Screen.setColorCorrectionAsJsonString"
        params = ["colorCorrection"]

    def getColorCorrectionAsJsonString() -> str:
        method = "Pixera.Screens.Screen.getColorCorrectionAsJsonString"
        params = [""]

    def getOutput() -> handle[]:
        method = "Pixera.Screens.Screen.getOutput"
        params = [""]

    def setBlackout(isActive: bool) -> None:
        method = "Pixera.Screens.Screen.setBlackout"
        params = ["isActive"]

    def getBlackout() -> bool:
        method = "Pixera.Screens.Screen.getBlackout"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Screens.Screen.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Screens.Screen.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Screens.Screen.getInstancePath"
        params = [""]

class StudioCamera:
    def getName() -> str:
        method = "Pixera.Screens.StudioCamera.getName"
        params = [""]

    def setPosition(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> None:
        method = "Pixera.Screens.StudioCamera.setPosition"
        params = ["xPos, yPos, zPos"]

    def getPosition(xPos: float, yPos: float, zPos: float) -> float[]:
        method = "Pixera.Screens.StudioCamera.getPosition"
        params = ["xPos, yPos, zPos"]

    def setRotation(xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> None:
        method = "Pixera.Screens.StudioCamera.setRotation"
        params = ["xRot, yRot, zRot"]

    def getRotation(xPos: float, yPos: float, zPos: float) -> float[]:
        method = "Pixera.Screens.StudioCamera.getRotation"
        params = ["xPos, yPos, zPos"]

    def setTransformation(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>, xRot: optional<float>, yRot: optional<float>, zRot: optional<float>, fov: optional<float>, aspectRatio: optional<float>) -> None:
        method = "Pixera.Screens.StudioCamera.setTransformation"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio"]

    def setTransformationAndLensProps(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, iris: float, k1: float, k2: float, centerX: float, centerY: float, panelWidth: float) -> None:
        method = "Pixera.Screens.StudioCamera.setTransformationAndLensProps"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth"]

    def setTransformationAndLensPropsExt(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, focalDistance: float, zoom: float, iris: float, k1: float, k2: float, k3: float, p1: float, p2: float, centerX: float, centerY: float, panelWidth: float, overscan: float) -> None:
        method = "Pixera.Screens.StudioCamera.setTransformationAndLensPropsExt"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, focalDistance, zoom, iris, k1, k2, k3, p1, p2, centerX, centerY, panelWidth, overscan"]

    def setTrackingInputPause(pause: bool) -> None:
        method = "Pixera.Screens.StudioCamera.setTrackingInputPause"
        params = ["pause"]

    def getTrackingInputPause() -> bool:
        method = "Pixera.Screens.StudioCamera.getTrackingInputPause"
        params = [""]

    def setUsePositionPropertiesFromTracking(pause: bool) -> None:
        method = "Pixera.Screens.StudioCamera.setUsePositionPropertiesFromTracking"
        params = ["pause"]

    def getUsePositionPropertiesFromTracking() -> bool:
        method = "Pixera.Screens.StudioCamera.getUsePositionPropertiesFromTracking"
        params = [""]

    def setUseRotationPropertiesFromTracking(pause: bool) -> None:
        method = "Pixera.Screens.StudioCamera.setUseRotationPropertiesFromTracking"
        params = ["pause"]

    def getUseRotationPropertiesFromTracking() -> bool:
        method = "Pixera.Screens.StudioCamera.getUseRotationPropertiesFromTracking"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Screens.StudioCamera.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Screens.StudioCamera.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Screens.StudioCamera.getInstancePath"
        params = [""]

class Perspective:
    def getName() -> str:
        method = "Pixera.Screens.Perspective.getName"
        params = [""]

    def setTransformation(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>, xRot: optional<float>, yRot: optional<float>, zRot: optional<float>, fov: optional<float>, aspectRatio: optional<float>) -> None:
        method = "Pixera.Screens.Perspective.setTransformation"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio"]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Screens.Perspective.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Screens.Perspective.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Screens.Perspective.getInstancePath"
        params = [""]

def getProjectorWithName(name: str) -> handle:
    method = "Pixera.Projectors.getProjectorWithName"
    params = ["name"]

    return [method,params,[name]]

def getProjectors() -> handle[]:
    method = "Pixera.Projectors.getProjectors"
    params = [""]

    return [method,params,[]]

def getProjectorNames() -> str[]:
    method = "Pixera.Projectors.getProjectorNames"
    params = [""]

    return [method,params,[]]

class Projector:
    def getPosition() -> ProjectorPosValues:
        method = "Pixera.Projectors.Projector.getPosition"
        params = [""]

    def setPosition(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> bool:
        method = "Pixera.Projectors.Projector.setPosition"
        params = ["xPos, yPos, zPos"]

    def getRotation() -> ProjectorPosValues:
        method = "Pixera.Projectors.Projector.getRotation"
        params = [""]

    def setRotation(xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> bool:
        method = "Pixera.Projectors.Projector.setRotation"
        params = ["xRot, yRot, zRot"]

    def getName() -> str:
        method = "Pixera.Projectors.Projector.getName"
        params = [""]

    def activateScreenMapping(screenId: float, isActive: bool) -> None:
        method = "Pixera.Projectors.Projector.activateScreenMapping"
        params = ["screenId, isActive"]

    def setBlackout(isActive: bool) -> None:
        method = "Pixera.Projectors.Projector.setBlackout"
        params = ["isActive"]

    def getBlackout() -> bool:
        method = "Pixera.Projectors.Projector.getBlackout"
        params = [""]

    def setSoftedgeVisible(screenName: str, visible: bool) -> None:
        method = "Pixera.Projectors.Projector.setSoftedgeVisible"
        params = ["screenName, visible"]

    def resetAllColorCorrections() -> None:
        method = "Pixera.Projectors.Projector.resetAllColorCorrections"
        params = [""]

    def setColorCorrectionWithPath(path: str, value: float) -> None:
        method = "Pixera.Projectors.Projector.setColorCorrectionWithPath"
        params = ["path, value"]

    def getColorCorrectionWithPath(path: str) -> float:
        method = "Pixera.Projectors.Projector.getColorCorrectionWithPath"
        params = ["path"]

    def setColorCorrectionAsJsonString(colorCorrection: str) -> None:
        method = "Pixera.Projectors.Projector.setColorCorrectionAsJsonString"
        params = ["colorCorrection"]

    def getColorCorrectionAsJsonString() -> str:
        method = "Pixera.Projectors.Projector.getColorCorrectionAsJsonString"
        params = [""]

    def getOutput() -> handle:
        method = "Pixera.Projectors.Projector.getOutput"
        params = [""]

    def setOutput(outputHandle: handle) -> None:
        method = "Pixera.Projectors.Projector.setOutput"
        params = ["outputHandle"]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Projectors.Projector.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Projectors.Projector.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Projectors.Projector.getInstancePath"
        params = [""]

def getResources() -> handle[]:
    method = "Pixera.Resources.getResources"
    params = [""]

    return [method,params,[]]

def getResourceFolderWithNamePath(namePath: str) -> handle:
    method = "Pixera.Resources.getResourceFolderWithNamePath"
    params = ["namePath"]

    return [method,params,[namePath]]

def getResourceFolders() -> handle[]:
    method = "Pixera.Resources.getResourceFolders"
    params = [""]

    return [method,params,[]]

def getTranscodingFolders() -> handle[]:
    method = "Pixera.Resources.getTranscodingFolders"
    params = [""]

    return [method,params,[]]

def getJsonDescrip() -> str:
    method = "Pixera.Resources.getJsonDescrip"
    params = [""]

    return [method,params,[]]

class ResourceFolder:
    def ref() -> handle:
        method = "Pixera.Resources.ResourceFolder.ref"
        params = [""]

    def getName() -> str:
        method = "Pixera.Resources.ResourceFolder.getName"
        params = [""]

    def setName(name: str) -> None:
        method = "Pixera.Resources.ResourceFolder.setName"
        params = ["name"]

    def getResourceFolders() -> handle[]:
        method = "Pixera.Resources.ResourceFolder.getResourceFolders"
        params = [""]

    def getResources() -> handle[]:
        method = "Pixera.Resources.ResourceFolder.getResources"
        params = [""]

    def getResourceAtIndex(index: int) -> handle:
        method = "Pixera.Resources.ResourceFolder.getResourceAtIndex"
        params = ["index"]

    def addResource(path: str) -> handle:
        method = "Pixera.Resources.ResourceFolder.addResource"
        params = ["path"]

    def addResourcesFromDirectory(path: str, removeOthers: bool, checkRedundancy: bool) -> handle[]:
        method = "Pixera.Resources.ResourceFolder.addResourcesFromDirectory"
        params = ["path, removeOthers, checkRedundancy"]

    def addResourcesFromDirectoryRemoveAssets(path: str, removeOthers: bool, checkRedundancy: bool) -> handle[]:
        method = "Pixera.Resources.ResourceFolder.addResourcesFromDirectoryRemoveAssets"
        params = ["path, removeOthers, checkRedundancy"]

    def addInternalResource(signature: str, resKind: int) -> handle:
        method = "Pixera.Resources.ResourceFolder.addInternalResource"
        params = ["signature, resKind"]

    def createFoldersFrom(path: str) -> None:
        method = "Pixera.Resources.ResourceFolder.createFoldersFrom"
        params = ["path"]

    def refreshResources() -> None:
        method = "Pixera.Resources.ResourceFolder.refreshResources"
        params = [""]

    def moveResourceToThis(id: float) -> None:
        method = "Pixera.Resources.ResourceFolder.moveResourceToThis"
        params = ["id"]

    def removeThis() -> None:
        method = "Pixera.Resources.ResourceFolder.removeThis"
        params = [""]

    def removeThisIncludingAssets() -> None:
        method = "Pixera.Resources.ResourceFolder.removeThisIncludingAssets"
        params = [""]

    def removeAllContents() -> None:
        method = "Pixera.Resources.ResourceFolder.removeAllContents"
        params = [""]

    def removeAllContentsIncludingAssets() -> None:
        method = "Pixera.Resources.ResourceFolder.removeAllContentsIncludingAssets"
        params = [""]

    def deleteAllContentsAssetsFromLiveSystem(apEntityLiveSystemHandle: handle) -> None:
        method = "Pixera.Resources.ResourceFolder.deleteAllContentsAssetsFromLiveSystem"
        params = ["apEntityLiveSystemHandle"]

    def resetDistributionTargets() -> None:
        method = "Pixera.Resources.ResourceFolder.resetDistributionTargets"
        params = [""]

    def changeDistributionTarget(apEntityLiveSystemHandle: handle, shouldDistribute: bool) -> None:
        method = "Pixera.Resources.ResourceFolder.changeDistributionTarget"
        params = ["apEntityLiveSystemHandle, shouldDistribute"]

    def replaceResourcesByString(searchString: str, replaceString: str, path: str) -> None:
        method = "Pixera.Resources.ResourceFolder.replaceResourcesByString"
        params = ["searchString, replaceString, path"]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Resources.ResourceFolder.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Resources.ResourceFolder.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Resources.ResourceFolder.getInstancePath"
        params = [""]

    def getDmxId() -> int:
        method = "Pixera.Resources.ResourceFolder.getDmxId"
        params = [""]

    def getCombinedDmxId() -> int:
        method = "Pixera.Resources.ResourceFolder.getCombinedDmxId"
        params = [""]

    def setDmxId(id: int) -> None:
        method = "Pixera.Resources.ResourceFolder.setDmxId"
        params = ["id"]

class TranscodingFolder:
    def getUsedTranscodingPreset() -> str:
        method = "Pixera.Resources.TranscodingFolder.getUsedTranscodingPreset"
        params = [""]

    def setUsedTranscodingPreset(preset: str) -> None:
        method = "Pixera.Resources.TranscodingFolder.setUsedTranscodingPreset"
        params = ["preset"]

    def getTranscodeAutomatically() -> bool:
        method = "Pixera.Resources.TranscodingFolder.getTranscodeAutomatically"
        params = [""]

    def setTranscodeAutomatically(autoTranscode: bool) -> None:
        method = "Pixera.Resources.TranscodingFolder.setTranscodeAutomatically"
        params = ["autoTranscode"]

    def getUseRxCacheAsDestination() -> bool:
        method = "Pixera.Resources.TranscodingFolder.getUseRxCacheAsDestination"
        params = [""]

    def setRxCacheAsDestination(useRxCache: bool) -> None:
        method = "Pixera.Resources.TranscodingFolder.setRxCacheAsDestination"
        params = ["useRxCache"]

    def getDestinationDirectory() -> str:
        method = "Pixera.Resources.TranscodingFolder.getDestinationDirectory"
        params = [""]

    def setDestinationDirectory(path: str) -> None:
        method = "Pixera.Resources.TranscodingFolder.setDestinationDirectory"
        params = ["path"]

class Resource:
    def ref() -> handle:
        method = "Pixera.Resources.Resource.ref"
        params = [""]

    def removeThis() -> None:
        method = "Pixera.Resources.Resource.removeThis"
        params = [""]

    def deleteFilesOnSystems() -> None:
        method = "Pixera.Resources.Resource.deleteFilesOnSystems"
        params = [""]

    def removeThisIncludingAssets() -> None:
        method = "Pixera.Resources.Resource.removeThisIncludingAssets"
        params = [""]

    def deleteAssetFromLiveSystem(apEntityLiveSystemHandle: handle) -> None:
        method = "Pixera.Resources.Resource.deleteAssetFromLiveSystem"
        params = ["apEntityLiveSystemHandle"]

    def resetDistributionTargets() -> None:
        method = "Pixera.Resources.Resource.resetDistributionTargets"
        params = [""]

    def changeDistributionTarget(apEntityLiveSystemHandle: handle, shouldDistribute: bool) -> None:
        method = "Pixera.Resources.Resource.changeDistributionTarget"
        params = ["apEntityLiveSystemHandle, shouldDistribute"]

    def getName() -> str:
        method = "Pixera.Resources.Resource.getName"
        params = [""]

    def setName(name: str) -> None:
        method = "Pixera.Resources.Resource.setName"
        params = ["name"]

    def getFps() -> float:
        method = "Pixera.Resources.Resource.getFps"
        params = [""]

    def getResolution() -> float[]:
        method = "Pixera.Resources.Resource.getResolution"
        params = [""]

    def getIsActive() -> bool:
        method = "Pixera.Resources.Resource.getIsActive"
        params = [""]

    def getVideoStreamModes() -> str[]:
        method = "Pixera.Resources.Resource.getVideoStreamModes"
        params = [""]

    def setVideoStreamMode(index: int) -> None:
        method = "Pixera.Resources.Resource.setVideoStreamMode"
        params = ["index"]

    def getId() -> float:
        method = "Pixera.Resources.Resource.getId"
        params = [""]

    def getDuration() -> float:
        method = "Pixera.Resources.Resource.getDuration"
        params = [""]

    def getType() -> str:
        method = "Pixera.Resources.Resource.getType"
        params = [""]

    def setCurrentVersion(version: str) -> None:
        method = "Pixera.Resources.Resource.setCurrentVersion"
        params = ["version"]

    def getCurrentVersion() -> str:
        method = "Pixera.Resources.Resource.getCurrentVersion"
        params = [""]

    def getVersions() -> str[]:
        method = "Pixera.Resources.Resource.getVersions"
        params = [""]

    def getVersionSuffix() -> str[]:
        method = "Pixera.Resources.Resource.getVersionSuffix"
        params = [""]

    def rescanVersions() -> None:
        method = "Pixera.Resources.Resource.rescanVersions"
        params = [""]

    def getThumbnailAsBase64() -> str:
        method = "Pixera.Resources.Resource.getThumbnailAsBase64"
        params = [""]

    def getHasPendingTransfer() -> bool:
        method = "Pixera.Resources.Resource.getHasPendingTransfer"
        params = [""]

    def getIsInUse() -> float:
        method = "Pixera.Resources.Resource.getIsInUse"
        params = [""]

    def getLastUsageBeginTime() -> float:
        method = "Pixera.Resources.Resource.getLastUsageBeginTime"
        params = [""]

    def getLastUsageBeginTimeAsString() -> str:
        method = "Pixera.Resources.Resource.getLastUsageBeginTimeAsString"
        params = [""]

    def getLastUsageEndTime() -> float:
        method = "Pixera.Resources.Resource.getLastUsageEndTime"
        params = [""]

    def getLastUsageEndTimeAsString() -> str:
        method = "Pixera.Resources.Resource.getLastUsageEndTimeAsString"
        params = [""]

    def getFilePath() -> str:
        method = "Pixera.Resources.Resource.getFilePath"
        params = [""]

    def setText(text: str) -> None:
        method = "Pixera.Resources.Resource.setText"
        params = ["text"]

    def getText() -> str:
        method = "Pixera.Resources.Resource.getText"
        params = [""]

    def setFontWithName(fontName: str) -> bool:
        method = "Pixera.Resources.Resource.setFontWithName"
        params = ["fontName"]

    def getFontName() -> str:
        method = "Pixera.Resources.Resource.getFontName"
        params = [""]

    def setFontWithPath(fontPath: str) -> bool:
        method = "Pixera.Resources.Resource.setFontWithPath"
        params = ["fontPath"]

    def setHorizontalTextAlignment(textAlignment: int) -> bool:
        method = "Pixera.Resources.Resource.setHorizontalTextAlignment"
        params = ["textAlignment"]

    def getHorizontalTextAlignment() -> int:
        method = "Pixera.Resources.Resource.getHorizontalTextAlignment"
        params = [""]

    def setVerticalTextAlignment(textAlignment: int) -> bool:
        method = "Pixera.Resources.Resource.setVerticalTextAlignment"
        params = ["textAlignment"]

    def getVerticalTextAlignment() -> int:
        method = "Pixera.Resources.Resource.getVerticalTextAlignment"
        params = [""]

    def setLineHeight(lineHeight: float) -> bool:
        method = "Pixera.Resources.Resource.setLineHeight"
        params = ["lineHeight"]

    def getLineHeight() -> float:
        method = "Pixera.Resources.Resource.getLineHeight"
        params = [""]

    def getTextMeasurementsWidthAndHeight() -> int[]:
        method = "Pixera.Resources.Resource.getTextMeasurementsWidthAndHeight"
        params = [""]

    def setUrl(url: str) -> None:
        method = "Pixera.Resources.Resource.setUrl"
        params = ["url"]

    def getUrl() -> str:
        method = "Pixera.Resources.Resource.getUrl"
        params = [""]

    def setColorTransformPath(colorTransformPath: str) -> None:
        method = "Pixera.Resources.Resource.setColorTransformPath"
        params = ["colorTransformPath"]

    def getColorTransformPath() -> str:
        method = "Pixera.Resources.Resource.getColorTransformPath"
        params = [""]

    def clearColorTransformPath() -> None:
        method = "Pixera.Resources.Resource.clearColorTransformPath"
        params = [""]

    def refresh(text: str) -> None:
        method = "Pixera.Resources.Resource.refresh"
        params = ["text"]

    def distribute() -> None:
        method = "Pixera.Resources.Resource.distribute"
        params = [""]

    def getDmxId() -> int:
        method = "Pixera.Resources.Resource.getDmxId"
        params = [""]

    def setDmxId(id: int) -> None:
        method = "Pixera.Resources.Resource.setDmxId"
        params = ["id"]

    def removeMultiresourceIndex(index: int) -> None:
        method = "Pixera.Resources.Resource.removeMultiresourceIndex"
        params = ["index"]

    def addMultiresourceItem(id: float) -> None:
        method = "Pixera.Resources.Resource.addMultiresourceItem"
        params = ["id"]

    def getMultiresourceItems() -> handle[]:
        method = "Pixera.Resources.Resource.getMultiresourceItems"
        params = [""]

    def replaceMultiresourceItemByIndex(index: int, id: float) -> None:
        method = "Pixera.Resources.Resource.replaceMultiresourceItemByIndex"
        params = ["index, id"]

    def setMultiresourceResolution(width: int, height: int) -> None:
        method = "Pixera.Resources.Resource.setMultiresourceResolution"
        params = ["width, height"]

    def setMultiresourceItemSizebyIndex(index: int, width: float, height: float) -> None:
        method = "Pixera.Resources.Resource.setMultiresourceItemSizebyIndex"
        params = ["index, width, height"]

    def setMultiresourceItemPositionbyIndex(index: int, x: float, y: float) -> None:
        method = "Pixera.Resources.Resource.setMultiresourceItemPositionbyIndex"
        params = ["index, x, y"]

    def setUseGradient(useGradient: bool) -> None:
        method = "Pixera.Resources.Resource.setUseGradient"
        params = ["useGradient"]

    def getUseGradient() -> bool:
        method = "Pixera.Resources.Resource.getUseGradient"
        params = [""]

    def setColors(argbCols: uint[], positions: float[], colNames: str[], useGradient: optional<bool>) -> None:
        method = "Pixera.Resources.Resource.setColors"
        params = ["argbCols, positions, colNames, useGradient"]

    def setColorAtIndex(index: int, red: int, green: int, blue: int, alpha: int, position: float, name: str, useGradient: optional<bool>) -> None:
        method = "Pixera.Resources.Resource.setColorAtIndex"
        params = ["index, red, green, blue, alpha, position, name, useGradient"]

    def getColorAtIndex(colorIndex: int) -> int:
        method = "Pixera.Resources.Resource.getColorAtIndex"
        params = ["colorIndex"]

    def getColorPositionAtIndex(colorIndex: int) -> float:
        method = "Pixera.Resources.Resource.getColorPositionAtIndex"
        params = ["colorIndex"]

    def launchVirtualWorld(action: str) -> None:
        method = "Pixera.Resources.Resource.launchVirtualWorld"
        params = ["action"]

    def getUnrealWorld() -> handle:
        method = "Pixera.Resources.Resource.getUnrealWorld"
        params = [""]

    def setMultiResourceItemRestrictedServiceIps(itemIndex: int, ipAdresses: str[]) -> None:
        method = "Pixera.Resources.Resource.setMultiResourceItemRestrictedServiceIps"
        params = ["itemIndex, ipAdresses"]

    def getMultiResourceItemRestrictedServiceIps(itemIndex: int) -> str[]:
        method = "Pixera.Resources.Resource.getMultiResourceItemRestrictedServiceIps"
        params = ["itemIndex"]

    def replace(path: str) -> None:
        method = "Pixera.Resources.Resource.replace"
        params = ["path"]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Resources.Resource.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Resources.Resource.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Resources.Resource.getInstancePath"
        params = [""]

    def transcodeWithExisitngPreset(presetName: str, useRxCache: bool, destinationPath: str, startFrame: int, endFrame: int, serviceId: uint) -> None:
        method = "Pixera.Resources.Resource.transcodeWithExisitngPreset"
        params = ["presetName, useRxCache, destinationPath, startFrame, endFrame, serviceId"]

    def transcodeWithSettings(settings: str, useRxCache: bool, destinationPath: str, startFrame: int, endFrame: int, serviceId: uint) -> None:
        method = "Pixera.Resources.Resource.transcodeWithSettings"
        params = ["settings, useRxCache, destinationPath, startFrame, endFrame, serviceId"]

    def moveToTranscodingFolder(folderPath: str) -> None:
        method = "Pixera.Resources.Resource.moveToTranscodingFolder"
        params = ["folderPath"]

class UnrealWorld:
    def getLevelNames() -> str[]:
        method = "Pixera.Resources.UnrealWorld.getLevelNames"
        params = [""]

    def loadLevel(levelName: str) -> None:
        method = "Pixera.Resources.UnrealWorld.loadLevel"
        params = ["levelName"]

    def getEventTriggerNames() -> str[]:
        method = "Pixera.Resources.UnrealWorld.getEventTriggerNames"
        params = [""]

    def triggerEventByName(triggerName: str) -> None:
        method = "Pixera.Resources.UnrealWorld.triggerEventByName"
        params = ["triggerName"]

    def createNDisplayConfig() -> None:
        method = "Pixera.Resources.UnrealWorld.createNDisplayConfig"
        params = [""]

    def runUnreal() -> None:
        method = "Pixera.Resources.UnrealWorld.runUnreal"
        params = [""]

    def killUnreal() -> None:
        method = "Pixera.Resources.UnrealWorld.killUnreal"
        params = [""]

    def getName() -> str:
        method = "Pixera.Resources.UnrealWorld.getName"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Resources.UnrealWorld.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Resources.UnrealWorld.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Resources.UnrealWorld.getInstancePath"
        params = [""]

def getTimelineAtIndex(index: int) -> handle:
    method = "Pixera.Timelines.getTimelineAtIndex"
    params = ["index"]

    return [method,params,[index]]

def getTimelineFromName(name: str) -> handle:
    method = "Pixera.Timelines.getTimelineFromName"
    params = ["name"]

    return [method,params,[name]]

def getTimelines() -> handle[]:
    method = "Pixera.Timelines.getTimelines"
    params = [""]

    return [method,params,[]]

def getTimelineNames() -> str[]:
    method = "Pixera.Timelines.getTimelineNames"
    params = [""]

    return [method,params,[]]

def getTimelinesSelected() -> handle[]:
    method = "Pixera.Timelines.getTimelinesSelected"
    params = [""]

    return [method,params,[]]

def createTimeline() -> handle:
    method = "Pixera.Timelines.createTimeline"
    params = [""]

    return [method,params,[]]

def getNodeFromId(id: float) -> handle:
    method = "Pixera.Timelines.getNodeFromId"
    params = ["id"]

    return [method,params,[id]]

class Timeline:
    def ref() -> handle:
        method = "Pixera.Timelines.Timeline.ref"
        params = [""]

    def removeThis() -> None:
        method = "Pixera.Timelines.Timeline.removeThis"
        params = [""]

    def duplicateThis(withoutClipsCues: optional<bool>) -> handle:
        method = "Pixera.Timelines.Timeline.duplicateThis"
        params = ["withoutClipsCues"]

    def selectThis() -> None:
        method = "Pixera.Timelines.Timeline.selectThis"
        params = [""]

    def getZoomFactor() -> float:
        method = "Pixera.Timelines.Timeline.getZoomFactor"
        params = [""]

    def setZoomFactor(zoomFactor: float) -> None:
        method = "Pixera.Timelines.Timeline.setZoomFactor"
        params = ["zoomFactor"]

    def getVerticalScrollOffset() -> int:
        method = "Pixera.Timelines.Timeline.getVerticalScrollOffset"
        params = [""]

    def setVerticalScrollOffset(offset: int) -> None:
        method = "Pixera.Timelines.Timeline.setVerticalScrollOffset"
        params = ["offset"]

    def getHorizontalScrollOffset() -> int:
        method = "Pixera.Timelines.Timeline.getHorizontalScrollOffset"
        params = [""]

    def setHorizontalScrollOffset(offset: int) -> None:
        method = "Pixera.Timelines.Timeline.setHorizontalScrollOffset"
        params = ["offset"]

    def moveInRenderOrder(moveDown: bool) -> None:
        method = "Pixera.Timelines.Timeline.moveInRenderOrder"
        params = ["moveDown"]

    def getLayers() -> handle[]:
        method = "Pixera.Timelines.Timeline.getLayers"
        params = [""]

    def getLayerNames() -> str[]:
        method = "Pixera.Timelines.Timeline.getLayerNames"
        params = [""]

    def getLayersSelected() -> handle[]:
        method = "Pixera.Timelines.Timeline.getLayersSelected"
        params = [""]

    def selectLayerByIndex(index: int) -> None:
        method = "Pixera.Timelines.Timeline.selectLayerByIndex"
        params = ["index"]

    def selectLayerByNames(layerNames: str[]) -> None:
        method = "Pixera.Timelines.Timeline.selectLayerByNames"
        params = ["layerNames"]

    def getLayerAtIndex(index: int) -> handle:
        method = "Pixera.Timelines.Timeline.getLayerAtIndex"
        params = ["index"]

    def createLayer() -> handle:
        method = "Pixera.Timelines.Timeline.createLayer"
        params = [""]

    def getCueInfosAsJsonString() -> str:
        method = "Pixera.Timelines.Timeline.getCueInfosAsJsonString"
        params = [""]

    def getCues() -> handle[]:
        method = "Pixera.Timelines.Timeline.getCues"
        params = [""]

    def getCueNames() -> str[]:
        method = "Pixera.Timelines.Timeline.getCueNames"
        params = [""]

    def getCueAtIndex(index: int) -> handle:
        method = "Pixera.Timelines.Timeline.getCueAtIndex"
        params = ["index"]

    def getCueFromName(name: str) -> handle:
        method = "Pixera.Timelines.Timeline.getCueFromName"
        params = ["name"]

    def getCueFromNumber(number: int) -> handle:
        method = "Pixera.Timelines.Timeline.getCueFromNumber"
        params = ["number"]

    def applyCueWithName(name: str) -> None:
        method = "Pixera.Timelines.Timeline.applyCueWithName"
        params = ["name"]

    def applyCueWithNumber(number: int) -> None:
        method = "Pixera.Timelines.Timeline.applyCueWithNumber"
        params = ["number"]

    def createCue(name: str, timeInFrames: float, operation: int) -> handle:
        method = "Pixera.Timelines.Timeline.createCue"
        params = ["name, timeInFrames, operation"]

    def removeCues() -> None:
        method = "Pixera.Timelines.Timeline.removeCues"
        params = [""]

    def createPauseCueBeforeSelectedClips() -> None:
        method = "Pixera.Timelines.Timeline.createPauseCueBeforeSelectedClips"
        params = [""]

    def play() -> None:
        method = "Pixera.Timelines.Timeline.play"
        params = [""]

    def pause() -> None:
        method = "Pixera.Timelines.Timeline.pause"
        params = [""]

    def stop() -> None:
        method = "Pixera.Timelines.Timeline.stop"
        params = [""]

    def toggleTransport() -> None:
        method = "Pixera.Timelines.Timeline.toggleTransport"
        params = [""]

    def store() -> None:
        method = "Pixera.Timelines.Timeline.store"
        params = [""]

    def reset() -> None:
        method = "Pixera.Timelines.Timeline.reset"
        params = [""]

    def getAttributes() -> TimelineAttributes:
        method = "Pixera.Timelines.Timeline.getAttributes"
        params = [""]

    def setCurrentFrame(time: int) -> bool:
        method = "Pixera.Timelines.Timeline.setCurrentFrame"
        params = ["time"]

    def setCurrentTime(time: int) -> None:
        method = "Pixera.Timelines.Timeline.setCurrentTime"
        params = ["time"]

    def getCurrentTime() -> int:
        method = "Pixera.Timelines.Timeline.getCurrentTime"
        params = [""]

    def scrubCurrentTime(frames: int) -> None:
        method = "Pixera.Timelines.Timeline.scrubCurrentTime"
        params = ["frames"]

    def CurrentTime(time: int, doSet: bool) -> int:
        method = "Pixera.Timelines.Timeline.CurrentTime"
        params = ["time, doSet"]

    def getCurrentHMSF() -> str:
        method = "Pixera.Timelines.Timeline.getCurrentHMSF"
        params = [""]

    def setTransportMode(mode: int) -> bool:
        method = "Pixera.Timelines.Timeline.setTransportMode"
        params = ["mode"]

    def getTransportMode() -> int:
        method = "Pixera.Timelines.Timeline.getTransportMode"
        params = [""]

    def setTimecodeInput(hour: int, minute: int, second: int, frame: int, elapsedTime: float, running: bool, freshMode: int, stateToken: int, format: int) -> float:
        method = "Pixera.Timelines.Timeline.setTimecodeInput"
        params = ["hour, minute, second, frame, elapsedTime, running, freshMode, stateToken, format"]

    def getFps() -> float:
        method = "Pixera.Timelines.Timeline.getFps"
        params = [""]

    def getName() -> str:
        method = "Pixera.Timelines.Timeline.getName"
        params = [""]

    def setName(name: str) -> None:
        method = "Pixera.Timelines.Timeline.setName"
        params = ["name"]

    def moveToNextCue() -> None:
        method = "Pixera.Timelines.Timeline.moveToNextCue"
        params = [""]

    def moveToNextCueIgnoreProperties() -> None:
        method = "Pixera.Timelines.Timeline.moveToNextCueIgnoreProperties"
        params = [""]

    def getCueNext() -> handle:
        method = "Pixera.Timelines.Timeline.getCueNext"
        params = [""]

    def moveToPreviousCue() -> None:
        method = "Pixera.Timelines.Timeline.moveToPreviousCue"
        params = [""]

    def moveToPreviousCueIgnoreProperties() -> None:
        method = "Pixera.Timelines.Timeline.moveToPreviousCueIgnoreProperties"
        params = [""]

    def getCuePrevious() -> handle:
        method = "Pixera.Timelines.Timeline.getCuePrevious"
        params = [""]

    def ignoreNextCue() -> None:
        method = "Pixera.Timelines.Timeline.ignoreNextCue"
        params = [""]

    def ignoreNextCueWithOperation(cueOperation: int) -> None:
        method = "Pixera.Timelines.Timeline.ignoreNextCueWithOperation"
        params = ["cueOperation"]

    def blendToTime(goalTime: float, blendDuration: float, preloadDelayInMilliseconds: optional<int>) -> None:
        method = "Pixera.Timelines.Timeline.blendToTime"
        params = ["goalTime, blendDuration, preloadDelayInMilliseconds"]

    def blendToTimeWithTransportMode(goalTime: float, blendDuration: float, transportMode: int, preloadDelayInMilliseconds: optional<int>) -> None:
        method = "Pixera.Timelines.Timeline.blendToTimeWithTransportMode"
        params = ["goalTime, blendDuration, transportMode, preloadDelayInMilliseconds"]

    def setBlendToTimeMode(mode: int) -> bool:
        method = "Pixera.Timelines.Timeline.setBlendToTimeMode"
        params = ["mode"]

    def setSpeedFactor(factor: float) -> None:
        method = "Pixera.Timelines.Timeline.setSpeedFactor"
        params = ["factor"]

    def getSpeedFactor() -> float:
        method = "Pixera.Timelines.Timeline.getSpeedFactor"
        params = [""]

    def setOpacity(value: float) -> None:
        method = "Pixera.Timelines.Timeline.setOpacity"
        params = ["value"]

    def getOpacity() -> float:
        method = "Pixera.Timelines.Timeline.getOpacity"
        params = [""]

    def startOpacityAnimation(fadeIn: bool, durationFrames: float) -> None:
        method = "Pixera.Timelines.Timeline.startOpacityAnimation"
        params = ["fadeIn, durationFrames"]

    def setSmpteMode(mode: int) -> None:
        method = "Pixera.Timelines.Timeline.setSmpteMode"
        params = ["mode"]

    def getSmpteMode() -> int:
        method = "Pixera.Timelines.Timeline.getSmpteMode"
        params = [""]

    def storeRecordedValues() -> None:
        method = "Pixera.Timelines.Timeline.storeRecordedValues"
        params = [""]

    def setSmpteInputBehaviour(mode: int) -> None:
        method = "Pixera.Timelines.Timeline.setSmpteInputBehaviour"
        params = ["mode"]

    def getSmpteInputBehaviour() -> int:
        method = "Pixera.Timelines.Timeline.getSmpteInputBehaviour"
        params = [""]

    def setSmpteOffset(time: float) -> None:
        method = "Pixera.Timelines.Timeline.setSmpteOffset"
        params = ["time"]

    def getSmpteOffset() -> float:
        method = "Pixera.Timelines.Timeline.getSmpteOffset"
        params = [""]

    def resetRecordedValues() -> None:
        method = "Pixera.Timelines.Timeline.resetRecordedValues"
        params = [""]

    def getTimelineInfosAsJsonString() -> str:
        method = "Pixera.Timelines.Timeline.getTimelineInfosAsJsonString"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Timelines.Timeline.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Timelines.Timeline.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Timelines.Timeline.getInstancePath"
        params = [""]

class Layer:
    def ref() -> handle:
        method = "Pixera.Timelines.Layer.ref"
        params = [""]

    def removeThis() -> None:
        method = "Pixera.Timelines.Layer.removeThis"
        params = [""]

    def getNodes() -> handle[]:
        method = "Pixera.Timelines.Layer.getNodes"
        params = [""]

    def getNodeWithName(name: str) -> handle:
        method = "Pixera.Timelines.Layer.getNodeWithName"
        params = ["name"]

    def getParamWithName(name: str) -> handle:
        method = "Pixera.Timelines.Layer.getParamWithName"
        params = ["name"]

    def getSpatialParametersAtTime(time: float) -> float[]:
        method = "Pixera.Timelines.Layer.getSpatialParametersAtTime"
        params = ["time"]

    def getTimeline() -> handle:
        method = "Pixera.Timelines.Layer.getTimeline"
        params = [""]

    def setName(name: str) -> None:
        method = "Pixera.Timelines.Layer.setName"
        params = ["name"]

    def getName() -> str:
        method = "Pixera.Timelines.Layer.getName"
        params = [""]

    def resetLayer() -> None:
        method = "Pixera.Timelines.Layer.resetLayer"
        params = [""]

    def getLayerJsonDescrip() -> str:
        method = "Pixera.Timelines.Layer.getLayerJsonDescrip"
        params = [""]

    def setLayerJsonDescrip(descrip: str, makeAllDominant: bool) -> None:
        method = "Pixera.Timelines.Layer.setLayerJsonDescrip"
        params = ["descrip, makeAllDominant"]

    def getJsonDescrip() -> str:
        method = "Pixera.Timelines.Layer.getJsonDescrip"
        params = [""]

    def initFromJsonDescrip(descrip: str) -> None:
        method = "Pixera.Timelines.Layer.initFromJsonDescrip"
        params = ["descrip"]

    def setOpacity(value: float) -> None:
        method = "Pixera.Timelines.Layer.setOpacity"
        params = ["value"]

    def getOpacity() -> float:
        method = "Pixera.Timelines.Layer.getOpacity"
        params = [""]

    def resetOpacity() -> None:
        method = "Pixera.Timelines.Layer.resetOpacity"
        params = [""]

    def setVolume(value: float) -> None:
        method = "Pixera.Timelines.Layer.setVolume"
        params = ["value"]

    def getVolume() -> float:
        method = "Pixera.Timelines.Layer.getVolume"
        params = [""]

    def resetVolume() -> None:
        method = "Pixera.Timelines.Layer.resetVolume"
        params = [""]

    def muteLayer() -> None:
        method = "Pixera.Timelines.Layer.muteLayer"
        params = [""]

    def unMuteLayer() -> None:
        method = "Pixera.Timelines.Layer.unMuteLayer"
        params = [""]

    def getIsLayerMuted() -> bool:
        method = "Pixera.Timelines.Layer.getIsLayerMuted"
        params = [""]

    def muteAudio() -> None:
        method = "Pixera.Timelines.Layer.muteAudio"
        params = [""]

    def unMuteAudio() -> None:
        method = "Pixera.Timelines.Layer.unMuteAudio"
        params = [""]

    def getIsAudioMuted() -> bool:
        method = "Pixera.Timelines.Layer.getIsAudioMuted"
        params = [""]

    def getDmxMuteState() -> int:
        method = "Pixera.Timelines.Layer.getDmxMuteState"
        params = [""]

    def setDmxMuteState(muteState: uint) -> None:
        method = "Pixera.Timelines.Layer.setDmxMuteState"
        params = ["muteState"]

    def toggleExplicitMute(flag: uint) -> None:
        method = "Pixera.Timelines.Layer.toggleExplicitMute"
        params = ["flag"]

    def setTransport(mode: int, loop: bool) -> None:
        method = "Pixera.Timelines.Layer.setTransport"
        params = ["mode, loop"]

    def getTransportMode() -> int:
        method = "Pixera.Timelines.Layer.getTransportMode"
        params = [""]

    def resetTransportMode() -> None:
        method = "Pixera.Timelines.Layer.resetTransportMode"
        params = [""]

    def getTransportLoop() -> bool:
        method = "Pixera.Timelines.Layer.getTransportLoop"
        params = [""]

    def assignResource(id: float) -> None:
        method = "Pixera.Timelines.Layer.assignResource"
        params = ["id"]

    def assignResourceWithFade(id: float, fadeDuration: float) -> None:
        method = "Pixera.Timelines.Layer.assignResourceWithFade"
        params = ["id, fadeDuration"]

    def getAssignedResource() -> handle:
        method = "Pixera.Timelines.Layer.getAssignedResource"
        params = [""]

    def resetAssignedResource() -> None:
        method = "Pixera.Timelines.Layer.resetAssignedResource"
        params = [""]

    def getAssignedModelResource() -> handle:
        method = "Pixera.Timelines.Layer.getAssignedModelResource"
        params = [""]

    def resetAssignedModelResource() -> None:
        method = "Pixera.Timelines.Layer.resetAssignedModelResource"
        params = [""]

    def getFxNames() -> str[]:
        method = "Pixera.Timelines.Layer.getFxNames"
        params = [""]

    def setFadeDurationDominantResourceChange(value: float) -> None:
        method = "Pixera.Timelines.Layer.setFadeDurationDominantResourceChange"
        params = ["value"]

    def getFadeDurationDominantResourceChange() -> float:
        method = "Pixera.Timelines.Layer.getFadeDurationDominantResourceChange"
        params = [""]

    def createClip() -> handle:
        method = "Pixera.Timelines.Layer.createClip"
        params = [""]

    def createClipAtTime(timeInFrames: float) -> handle:
        method = "Pixera.Timelines.Layer.createClipAtTime"
        params = ["timeInFrames"]

    def controlClipBorder(clip: handle, isEnter: bool, isIncremental: bool, entryTime: float) -> None:
        method = "Pixera.Timelines.Layer.controlClipBorder"
        params = ["clip, isEnter, isIncremental, entryTime"]

    def getClipAtIndex(index: int) -> handle:
        method = "Pixera.Timelines.Layer.getClipAtIndex"
        params = ["index"]

    def getClips() -> handle[]:
        method = "Pixera.Timelines.Layer.getClips"
        params = [""]

    def getClipCurrent(offset: int) -> handle:
        method = "Pixera.Timelines.Layer.getClipCurrent"
        params = ["offset"]

    def getClipsSelected() -> handle[]:
        method = "Pixera.Timelines.Layer.getClipsSelected"
        params = [""]

    def removeClips() -> None:
        method = "Pixera.Timelines.Layer.removeClips"
        params = [""]

    def setHomeScreenFromScreenName(screenName: str) -> None:
        method = "Pixera.Timelines.Layer.setHomeScreenFromScreenName"
        params = ["screenName"]

    def getHomeScreenName() -> str:
        method = "Pixera.Timelines.Layer.getHomeScreenName"
        params = [""]

    def setBlendMode(blendMode: str) -> None:
        method = "Pixera.Timelines.Layer.setBlendMode"
        params = ["blendMode"]

    def getBlendMode() -> str:
        method = "Pixera.Timelines.Layer.getBlendMode"
        params = [""]

    def addEffectById(id: float) -> None:
        method = "Pixera.Timelines.Layer.addEffectById"
        params = ["id"]

    def setPreloadPermanently(doPreloadPermanently: bool) -> None:
        method = "Pixera.Timelines.Layer.setPreloadPermanently"
        params = ["doPreloadPermanently"]

    def getPreloadPermanently() -> bool:
        method = "Pixera.Timelines.Layer.getPreloadPermanently"
        params = [""]

    def setRestrictToServiceWithIps(doRestrict: bool, ipAdresses: str[]) -> None:
        method = "Pixera.Timelines.Layer.setRestrictToServiceWithIps"
        params = ["doRestrict, ipAdresses"]

    def getRestrictToService() -> bool:
        method = "Pixera.Timelines.Layer.getRestrictToService"
        params = [""]

    def getRestrictedServiceIps() -> str[]:
        method = "Pixera.Timelines.Layer.getRestrictedServiceIps"
        params = [""]

    def getOffsets() -> float[]:
        method = "Pixera.Timelines.Layer.getOffsets"
        params = [""]

    def setOffsets(x: optional<float>, y: optional<float>, z: optional<float>, xr: optional<float>, yr: optional<float>, zr: optional<float>, xScale: optional<float>, yScale: optional<float>, zScale: optional<float>) -> None:
        method = "Pixera.Timelines.Layer.setOffsets"
        params = ["x, y, z, xr, yr, zr, xScale, yScale, zScale"]

    def setCurrentValuesToOffset(typeIndex: int, resetDominant: optional<bool>, removeKeyframesClips: optional<bool>) -> None:
        method = "Pixera.Timelines.Layer.setCurrentValuesToOffset"
        params = ["typeIndex, resetDominant, removeKeyframesClips"]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Timelines.Layer.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Timelines.Layer.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Timelines.Layer.getInstancePath"
        params = [""]

class Clip:
    def getId() -> float:
        method = "Pixera.Timelines.Clip.getId"
        params = [""]

    def removeThis() -> None:
        method = "Pixera.Timelines.Clip.removeThis"
        params = [""]

    def getTimeline() -> handle:
        method = "Pixera.Timelines.Clip.getTimeline"
        params = [""]

    def setTime(time: float) -> None:
        method = "Pixera.Timelines.Clip.setTime"
        params = ["time"]

    def getTime() -> float:
        method = "Pixera.Timelines.Clip.getTime"
        params = [""]

    def setDuration(duration: float) -> None:
        method = "Pixera.Timelines.Clip.setDuration"
        params = ["duration"]

    def getDuration() -> float:
        method = "Pixera.Timelines.Clip.getDuration"
        params = [""]

    def setLabel(label: str) -> None:
        method = "Pixera.Timelines.Clip.setLabel"
        params = ["label"]

    def getLabel() -> str:
        method = "Pixera.Timelines.Clip.getLabel"
        params = [""]

    def getPlayMode() -> int:
        method = "Pixera.Timelines.Clip.getPlayMode"
        params = [""]

    def setPlayMode(playMode: int) -> None:
        method = "Pixera.Timelines.Clip.setPlayMode"
        params = ["playMode"]

    def getSpeed() -> float:
        method = "Pixera.Timelines.Clip.getSpeed"
        params = [""]

    def setSpeed(speed: float) -> None:
        method = "Pixera.Timelines.Clip.setSpeed"
        params = ["speed"]

    def getBlendFrames() -> bool:
        method = "Pixera.Timelines.Clip.getBlendFrames"
        params = [""]

    def setBlendFrames(doFrameblending: bool) -> None:
        method = "Pixera.Timelines.Clip.setBlendFrames"
        params = ["doFrameblending"]

    def getInpoint() -> float:
        method = "Pixera.Timelines.Clip.getInpoint"
        params = [""]

    def setInpoint(inpoint: float) -> None:
        method = "Pixera.Timelines.Clip.setInpoint"
        params = ["inpoint"]

    def getOutpoint() -> float:
        method = "Pixera.Timelines.Clip.getOutpoint"
        params = [""]

    def setOutpoint(inpoint: float) -> None:
        method = "Pixera.Timelines.Clip.setOutpoint"
        params = ["inpoint"]

    def assignResource(resId: float, setToResourceDuration: optional<bool>) -> None:
        method = "Pixera.Timelines.Clip.assignResource"
        params = ["resId, setToResourceDuration"]

    def getAssignedResource() -> handle:
        method = "Pixera.Timelines.Clip.getAssignedResource"
        params = [""]

    def setToResourceDuration() -> None:
        method = "Pixera.Timelines.Clip.setToResourceDuration"
        params = [""]

    def createEvent(namePath: str, time: float, value: float) -> None:
        method = "Pixera.Timelines.Clip.createEvent"
        params = ["namePath, time, value"]

    def createEventInPixelSpace(namePath: str, time: float, value: float) -> None:
        method = "Pixera.Timelines.Clip.createEventInPixelSpace"
        params = ["namePath, time, value"]

    def removeEvent(namePath: str, time: float) -> None:
        method = "Pixera.Timelines.Clip.removeEvent"
        params = ["namePath, time"]

    def createPauseCueBeforeClip() -> handle:
        method = "Pixera.Timelines.Clip.createPauseCueBeforeClip"
        params = [""]

    def setColorTransformPath(colorTransformPath: str) -> None:
        method = "Pixera.Timelines.Clip.setColorTransformPath"
        params = ["colorTransformPath"]

    def getColorTransformPath() -> str:
        method = "Pixera.Timelines.Clip.getColorTransformPath"
        params = [""]

    def clearColorTransformPath() -> None:
        method = "Pixera.Timelines.Clip.clearColorTransformPath"
        params = [""]

    def getKeyframesAsJsonString() -> str:
        method = "Pixera.Timelines.Clip.getKeyframesAsJsonString"
        params = [""]

class Node:
    def getParameters() -> handle[]:
        method = "Pixera.Timelines.Node.getParameters"
        params = [""]

    def getName() -> str:
        method = "Pixera.Timelines.Node.getName"
        params = [""]

    def getParamWithName(name: str) -> handle:
        method = "Pixera.Timelines.Node.getParamWithName"
        params = ["name"]

    def setValues(values: float[]) -> None:
        method = "Pixera.Timelines.Node.setValues"
        params = ["values"]

    def getValues() -> float[]:
        method = "Pixera.Timelines.Node.getValues"
        params = [""]

    def resetValues() -> None:
        method = "Pixera.Timelines.Node.resetValues"
        params = [""]

    def storeValues() -> None:
        method = "Pixera.Timelines.Node.storeValues"
        params = [""]

    def mute() -> None:
        method = "Pixera.Timelines.Node.mute"
        params = [""]

    def unMute() -> None:
        method = "Pixera.Timelines.Node.unMute"
        params = [""]

    def getIsMuted() -> bool:
        method = "Pixera.Timelines.Node.getIsMuted"
        params = [""]

    def getTimeline() -> handle:
        method = "Pixera.Timelines.Node.getTimeline"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Timelines.Node.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Timelines.Node.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Timelines.Node.getInstancePath"
        params = [""]

class Param:
    def getName() -> str:
        method = "Pixera.Timelines.Param.getName"
        params = [""]

    def getIsChannel() -> bool:
        method = "Pixera.Timelines.Param.getIsChannel"
        params = [""]

    def setValue(value: timelineParamValue) -> None:
        method = "Pixera.Timelines.Param.setValue"
        params = ["value"]

    def setValueRelativ(value: float) -> None:
        method = "Pixera.Timelines.Param.setValueRelativ"
        params = ["value"]

    def getValue() -> timelineParamValue:
        method = "Pixera.Timelines.Param.getValue"
        params = [""]

    def resetValue() -> None:
        method = "Pixera.Timelines.Param.resetValue"
        params = [""]

    def storeValue() -> None:
        method = "Pixera.Timelines.Param.storeValue"
        params = [""]

    def setTransportAttributes(mode: int, speed: float, loop: bool, inpoint: int, outpoint: int) -> None:
        method = "Pixera.Timelines.Param.setTransportAttributes"
        params = ["mode, speed, loop, inpoint, outpoint"]

    def getAttributes() -> TransportAttributes:
        method = "Pixera.Timelines.Param.getAttributes"
        params = [""]

    def mute() -> None:
        method = "Pixera.Timelines.Param.mute"
        params = [""]

    def unMute() -> None:
        method = "Pixera.Timelines.Param.unMute"
        params = [""]

    def getIsMuted() -> bool:
        method = "Pixera.Timelines.Param.getIsMuted"
        params = [""]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Timelines.Param.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Timelines.Param.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Timelines.Param.getInstancePath"
        params = [""]

class Cue:
    def removeThis() -> None:
        method = "Pixera.Timelines.Cue.removeThis"
        params = [""]

    def apply() -> None:
        method = "Pixera.Timelines.Cue.apply"
        params = [""]

    def blendToThis(blendDurationInSeconds: float) -> None:
        method = "Pixera.Timelines.Cue.blendToThis"
        params = ["blendDurationInSeconds"]

    def getAttributes() -> CueAttributes:
        method = "Pixera.Timelines.Cue.getAttributes"
        params = [""]

    def getTimeline() -> handle:
        method = "Pixera.Timelines.Cue.getTimeline"
        params = [""]

    def getIndex() -> int:
        method = "Pixera.Timelines.Cue.getIndex"
        params = [""]

    def getName() -> str:
        method = "Pixera.Timelines.Cue.getName"
        params = [""]

    def setName(name: str) -> bool:
        method = "Pixera.Timelines.Cue.setName"
        params = ["name"]

    def getNote() -> str:
        method = "Pixera.Timelines.Cue.getNote"
        params = [""]

    def setNote(note: str) -> bool:
        method = "Pixera.Timelines.Cue.setNote"
        params = ["note"]

    def getOperation() -> int:
        method = "Pixera.Timelines.Cue.getOperation"
        params = [""]

    def setOperation(operation: int) -> bool:
        method = "Pixera.Timelines.Cue.setOperation"
        params = ["operation"]

    def getJumpMode() -> int:
        method = "Pixera.Timelines.Cue.getJumpMode"
        params = [""]

    def setJumpMode(jumpMode: int) -> bool:
        method = "Pixera.Timelines.Cue.setJumpMode"
        params = ["jumpMode"]

    def getJumpGoalTime() -> float:
        method = "Pixera.Timelines.Cue.getJumpGoalTime"
        params = [""]

    def setJumpGoalTime(time: float) -> bool:
        method = "Pixera.Timelines.Cue.setJumpGoalTime"
        params = ["time"]

    def getJumpGoalLabel() -> str:
        method = "Pixera.Timelines.Cue.getJumpGoalLabel"
        params = [""]

    def getJumpGoalCue() -> handle:
        method = "Pixera.Timelines.Cue.getJumpGoalCue"
        params = [""]

    def setJumpGoalLabel(jumpGoalLabel: str) -> bool:
        method = "Pixera.Timelines.Cue.setJumpGoalLabel"
        params = ["jumpGoalLabel"]

    def getNumber() -> int:
        method = "Pixera.Timelines.Cue.getNumber"
        params = [""]

    def setNumber(number: int) -> None:
        method = "Pixera.Timelines.Cue.setNumber"
        params = ["number"]

    def getWaitDuration() -> float:
        method = "Pixera.Timelines.Cue.getWaitDuration"
        params = [""]

    def setWaitDuration(time: float) -> bool:
        method = "Pixera.Timelines.Cue.setWaitDuration"
        params = ["time"]

    def getBlendDuration() -> float:
        method = "Pixera.Timelines.Cue.getBlendDuration"
        params = [""]

    def setBlendDuration(timeInFrames: float) -> bool:
        method = "Pixera.Timelines.Cue.setBlendDuration"
        params = ["timeInFrames"]

    def getTime() -> float:
        method = "Pixera.Timelines.Cue.getTime"
        params = [""]

    def setTime(time: float) -> bool:
        method = "Pixera.Timelines.Cue.setTime"
        params = ["time"]

    def getTimelineToTriggerName() -> str:
        method = "Pixera.Timelines.Cue.getTimelineToTriggerName"
        params = [""]

    def setTimelineToTrigger(nameTimeline: str) -> bool:
        method = "Pixera.Timelines.Cue.setTimelineToTrigger"
        params = ["nameTimeline"]

    def getTimelineTriggerMode() -> int:
        method = "Pixera.Timelines.Cue.getTimelineTriggerMode"
        params = [""]

    def setTimelineTriggerMode(mode: int) -> bool:
        method = "Pixera.Timelines.Cue.setTimelineTriggerMode"
        params = ["mode"]

    def getTimelineTriggerApplyTime() -> float:
        method = "Pixera.Timelines.Cue.getTimelineTriggerApplyTime"
        params = [""]

    def setTimelineTriggerApplyTime(time: float) -> bool:
        method = "Pixera.Timelines.Cue.setTimelineTriggerApplyTime"
        params = ["time"]

    def setTimelineTriggerApplyCue(goalCueLabel: str) -> bool:
        method = "Pixera.Timelines.Cue.setTimelineTriggerApplyCue"
        params = ["goalCueLabel"]

    def getCountdown() -> float:
        method = "Pixera.Timelines.Cue.getCountdown"
        params = [""]

    def getCountdownHMSF() -> str:
        method = "Pixera.Timelines.Cue.getCountdownHMSF"
        params = [""]

    def setCommand(conveyorName: str, commandData: str) -> None:
        method = "Pixera.Timelines.Cue.setCommand"
        params = ["conveyorName, commandData"]

    def getInst(instancePath: str) -> handle:
        method = "Pixera.Timelines.Cue.getInst"
        params = ["instancePath"]

    def getHandleFromInstancePath(instancePath: str) -> handle:
        method = "Pixera.Timelines.Cue.getHandleFromInstancePath"
        params = ["instancePath"]

    def getInstancePath() -> str:
        method = "Pixera.Timelines.Cue.getInstancePath"
        params = [""]

def setMarkerPositions(positions: float[], markerIds: int[]) -> None:
    method = "Pixera.Calibration.setMarkerPositions"
    params = ["positions, markerIds"]

    return [method,params,[positions, markerIds]]

def loadDeviceUi(devicePath: str) -> None:
    method = "Pixera.WebViews.loadDeviceUi"
    params = ["devicePath"]

    return [method,params,[devicePath]]

def activatePreviousFunc() -> None:
    method = "Pixera.WebViews.activatePreviousFunc"
    params = [""]

    return [method,params,[]]

def activateNextFunc() -> None:
    method = "Pixera.WebViews.activateNextFunc"
    params = [""]

    return [method,params,[]]

def getLastActivatedFunc() -> str:
    method = "Pixera.WebViews.getLastActivatedFunc"
    params = [""]

    return [method,params,[]]

def deviceActivated(devicePath: str, withSelection: bool) -> None:
    method = "Pixera.WebViews.deviceActivated"
    params = ["devicePath, withSelection"]

    return [method,params,[devicePath, withSelection]]

def funcActivated(funcPath: str, withSelection: bool) -> None:
    method = "Pixera.WebViews.funcActivated"
    params = ["funcPath, withSelection"]

    return [method,params,[funcPath, withSelection]]

def setFuncBodyState(funcPath: str, state: str) -> None:
    method = "Pixera.WebViews.setFuncBodyState"
    params = ["funcPath, state"]

    return [method,params,[funcPath, state]]

def getFuncBodyState(funcPath: str) -> str:
    method = "Pixera.WebViews.getFuncBodyState"
    params = ["funcPath"]

    return [method,params,[funcPath]]

def setTag(tag: str, text: str) -> None:
    method = "Pixera.WebViews.setTag"
    params = ["tag, text"]

    return [method,params,[tag, text]]

def setEditorIsUsingBlocks(useBlocks: bool) -> None:
    method = "Pixera.WebViews.setEditorIsUsingBlocks"
    params = ["useBlocks"]

    return [method,params,[useBlocks]]

def getComboBoxWithId(id: float) -> handle:
    method = "Pixera.Ui.getComboBoxWithId"
    params = ["id"]

    return [method,params,[id]]

def setAppMode(mode: int) -> None:
    method = "Pixera.Ui.setAppMode"
    params = ["mode"]

    return [method,params,[mode]]

def getAppMode() -> int:
    method = "Pixera.Ui.getAppMode"
    params = [""]

    return [method,params,[]]

def getDisplayTestpattern() -> bool:
    method = "Pixera.Ui.getDisplayTestpattern"
    params = [""]

    return [method,params,[]]

def setDisplayTestpattern(display: bool) -> None:
    method = "Pixera.Ui.setDisplayTestpattern"
    params = ["display"]

    return [method,params,[display]]

def getPreviewCameraAsJsonString() -> str:
    method = "Pixera.Ui.getPreviewCameraAsJsonString"
    params = [""]

    return [method,params,[]]

def setPreviewCameraAsJsonString(cameraFrustrumStateString: str) -> None:
    method = "Pixera.Ui.setPreviewCameraAsJsonString"
    params = ["cameraFrustrumStateString"]

    return [method,params,[cameraFrustrumStateString]]

def setDisableContentRendering(state: bool) -> None:
    method = "Pixera.Ui.setDisableContentRendering"
    params = ["state"]

    return [method,params,[state]]

def getIsContentRenderingDisabled() -> bool:
    method = "Pixera.Ui.getIsContentRenderingDisabled"
    params = [""]

    return [method,params,[]]

def setDisableWorkspaceRendering(state: bool) -> None:
    method = "Pixera.Ui.setDisableWorkspaceRendering"
    params = ["state"]

    return [method,params,[state]]

def getIsWorkspaceRenderingDisabled() -> bool:
    method = "Pixera.Ui.getIsWorkspaceRenderingDisabled"
    params = [""]

    return [method,params,[]]

class ComboBox:
    def clear() -> None:
        method = "Pixera.Ui.ComboBox.clear"
        params = [""]

    def addItem(item: str, id: int) -> None:
        method = "Pixera.Ui.ComboBox.addItem"
        params = ["item, id"]

    def setSelectedId(id: int) -> None:
        method = "Pixera.Ui.ComboBox.setSelectedId"
        params = ["id"]

    def getSelectedId() -> int:
        method = "Pixera.Ui.ComboBox.getSelectedId"
        params = [""]

def setRegistered(hdls: handle[], expectedFrequency: int, dampingMs: int, usageHints: str[]) -> None:
    method = "Pixera.Direct.setRegistered"
    params = ["hdls, expectedFrequency, dampingMs, usageHints"]

    return [method,params,[hdls, expectedFrequency, dampingMs, usageHints]]

def reloadRegistered() -> None:
    method = "Pixera.Direct.reloadRegistered"
    params = [""]

    return [method,params,[]]

def registerScreen(name: str, expectedFrequency: int, dampingMs: int) -> handle:
    method = "Pixera.Direct.registerScreen"
    params = ["name, expectedFrequency, dampingMs"]

    return [method,params,[name, expectedFrequency, dampingMs]]

def registerParam(instancePath: str) -> handle:
    method = "Pixera.Direct.registerParam"
    params = ["instancePath"]

    return [method,params,[instancePath]]

def registerCamera(cameraName: str, expectedFrequency: int) -> handle:
    method = "Pixera.Direct.registerCamera"
    params = ["cameraName, expectedFrequency"]

    return [method,params,[cameraName, expectedFrequency]]

def registerPerspective(screenName: str, expectedFrequency: int) -> handle:
    method = "Pixera.Direct.registerPerspective"
    params = ["screenName, expectedFrequency"]

    return [method,params,[screenName, expectedFrequency]]

class Screen:
    def setPosition(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>) -> None:
        method = "Pixera.Direct.Screen.setPosition"
        params = ["xPos, yPos, zPos"]

    def setRotation(xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> None:
        method = "Pixera.Direct.Screen.setRotation"
        params = ["xRot, yRot, zRot"]

    def setPosRot(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>, xRot: optional<float>, yRot: optional<float>, zRot: optional<float>) -> None:
        method = "Pixera.Direct.Screen.setPosRot"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot"]

    def setPosRotScale(xPos: optional<float>, yPos: optional<float>, zPos: optional<float>, xRot: optional<float>, yRot: optional<float>, zRot: optional<float>, xScale: optional<float>, yScale: optional<float>, zScale: optional<float>) -> None:
        method = "Pixera.Direct.Screen.setPosRotScale"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, xScale, yScale, zScale"]

    def enableLogging(enable: bool) -> None:
        method = "Pixera.Direct.Screen.enableLogging"
        params = ["enable"]

class Param:
    def setValue(value: float) -> None:
        method = "Pixera.Direct.Param.setValue"
        params = ["value"]

    def enableLogging(enable: bool) -> None:
        method = "Pixera.Direct.Param.enableLogging"
        params = ["enable"]

class Camera:
    def setPosition(xPos: float, yPos: float, zPos: float) -> None:
        method = "Pixera.Direct.Camera.setPosition"
        params = ["xPos, yPos, zPos"]

    def setRotation(xRot: float, yRot: float, zRot: float) -> None:
        method = "Pixera.Direct.Camera.setRotation"
        params = ["xRot, yRot, zRot"]

    def setTransformation(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float) -> None:
        method = "Pixera.Direct.Camera.setTransformation"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio"]

    def setTransformationAndLensProps(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, iris: float, k1: float, k2: float, centerX: float, centerY: float, panelWidth: float) -> None:
        method = "Pixera.Direct.Camera.setTransformationAndLensProps"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth"]

    def setTransformationAndLensPropsExt(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, focalDistance: float, zoom: float, iris: float, k1: float, k2: float, k3: float, p1: float, p2: float, centerX: float, centerY: float, panelWidth: float, overscan: float) -> None:
        method = "Pixera.Direct.Camera.setTransformationAndLensPropsExt"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, focalDistance, zoom, iris, k1, k2, k3, p1, p2, centerX, centerY, panelWidth, overscan"]

class Perspective:
    def setTransformation(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float) -> None:
        method = "Pixera.Direct.Perspective.setTransformation"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio"]

    def setTransformationAndLensProps(xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, iris: float, k1: float, k2: float, centerX: float, centerY: float, panelWidth: float) -> None:
        method = "Pixera.Direct.Perspective.setTransformationAndLensProps"
        params = ["xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth"]

def getSupportedUnrealPluginVersion() -> int:
    method = "Pixera.Unreal.Utility.getSupportedUnrealPluginVersion"
    params = [""]

    return [method,params,[]]

