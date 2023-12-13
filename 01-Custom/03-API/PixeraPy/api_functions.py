from typing import Optional, List
class uint:
    pass

class handle:
    pass

class ScreenPosValues:
    pass

class ProjectorPosValues:
    pass

class TimelineAttributes:
    pass

class timelineParamValue:
    pass

class TransportAttributes:
    pass

class CueAttributes:
    pass

class API:
    @staticmethod
    def getApiRevision() -> int:
        method = "Pixera.Utility.getApiRevision"
        params = []
        return [method, params, []]

    @staticmethod
    def getHasFunction(functionName: str) -> bool:
        method = "Pixera.Utility.getHasFunction"
        params = ["functionName"]
        return [method, params, [functionName]]

    @staticmethod
    def outputDebug(message: str) -> str:
        method = "Pixera.Utility.outputDebug"
        params = ["message"]
        return [method, params, [message]]

    @staticmethod
    def getLicenseJson() -> str:
        method = "Pixera.Utility.getLicenseJson"
        params = []
        return [method, params, []]

    @staticmethod
    def getCurrentTime() -> float:
        method = "Pixera.Utility.getCurrentTime"
        params = []
        return [method, params, []]

    @staticmethod
    def getCurrentTimeAsString() -> str:
        method = "Pixera.Utility.getCurrentTimeAsString"
        params = []
        return [method, params, []]

    @staticmethod
    def noop() -> None:
        method = "Pixera.Utility.noop"
        params = []
        return [method, params, []]

    @staticmethod
    def requestCallback(functionName: str) -> None:
        method = "Pixera.Utility.requestCallback"
        params = ["functionName"]
        return [method, params, [functionName]]

    @staticmethod
    def readFileString(path: str) -> str:
        method = "Pixera.Utility.readFileString"
        params = ["path"]
        return [method, params, [path]]

    @staticmethod
    def writeFileString(path: str, fileStr: str) -> None:
        method = "Pixera.Utility.writeFileString"
        params = ["path", "fileStr"]
        return [method, params, [path, fileStr]]

    @staticmethod
    def getAccessRecipe(hdlPath: str) -> str:
        method = "Pixera.Utility.getAccessRecipe"
        params = ["hdlPath"]
        return [method, params, [hdlPath]]

    @staticmethod
    def pollMonitoring() -> str:
        method = "Pixera.Utility.pollMonitoring"
        params = []
        return [method, params, []]

    @staticmethod
    def unsubscribeMonitoringSubject(subject: str) -> bool:
        method = "Pixera.Utility.unsubscribeMonitoringSubject"
        params = ["subject"]
        return [method, params, [subject]]

    @staticmethod
    def subscribeMonitoringSubject(subject: str) -> bool:
        method = "Pixera.Utility.subscribeMonitoringSubject"
        params = ["subject"]
        return [method, params, [subject]]

    @staticmethod
    def setMonitoringEventMode(mode: str) -> bool:
        method = "Pixera.Utility.setMonitoringEventMode"
        params = ["mode"]
        return [method, params, [mode]]

    @staticmethod
    def monitoringEvent(eventDescription: str) -> None:
        method = "Pixera.Utility.monitoringEvent"
        params = ["eventDescription"]
        return [method, params, [eventDescription]]

    @staticmethod
    def setShowContextInReplies(doShow: bool) -> bool:
        method = "Pixera.Utility.setShowContextInReplies"
        params = ["doShow"]
        return [method, params, [doShow]]

    @staticmethod
    def setMonitoringHasDelimiter(hasDelimiter: bool) -> bool:
        method = "Pixera.Utility.setMonitoringHasDelimiter"
        params = ["hasDelimiter"]
        return [method, params, [hasDelimiter]]

    @staticmethod
    def runJsScript(jsFunction: str, jsCode: str) -> str:
        method = "Pixera.Utility.runJsScript"
        params = ["jsFunction", "jsCode"]
        return [method, params, [jsFunction, jsCode]]

    @staticmethod
    def dynamicRebuildFromJsonDescription(deviceName: str, jsonDescription: str, folder: str) -> None:
        method = "Pixera.Utility.dynamicRebuildFromJsonDescription"
        params = ["deviceName", "jsonDescription", "folder"]
        return [method, params, [deviceName, jsonDescription, folder]]

    @staticmethod
    def getConveyor(conveyorName: str) -> handle:
        method = "Pixera.Network.getConveyor"
        params = ["conveyorName"]
        return [method, params, [conveyorName]]

    class Conveyor:
        @staticmethod
        def sendString(handle: handle, str: str) -> None:
            method = "Pixera.Network.Conveyor.sendString"
            params = ["handle, str"]

            return [method, params, [handle, str]]

    @staticmethod
    def setTransportModeOnTimelineAtIndex(index: int, mode: int) -> bool:
        method = "Pixera.Compound.setTransportModeOnTimelineAtIndex"
        params = ["index", "mode"]
        return [method, params, [index, mode]]

    @staticmethod
    def setTransportModeOnTimeline(timelineName: str, mode: int) -> None:
        method = "Pixera.Compound.setTransportModeOnTimeline"
        params = ["timelineName", "mode"]
        return [method, params, [timelineName, mode]]

    @staticmethod
    def toggleTransport(timelineName: str) -> None:
        method = "Pixera.Compound.toggleTransport"
        params = ["timelineName"]
        return [method, params, [timelineName]]

    @staticmethod
    def getTransportModeOnTimeline(timelineName: str) -> int:
        method = "Pixera.Compound.getTransportModeOnTimeline"
        params = ["timelineName"]
        return [method, params, [timelineName]]

    @staticmethod
    def startFirstTimeline() -> None:
        method = "Pixera.Compound.startFirstTimeline"
        params = []
        return [method, params, []]

    @staticmethod
    def pauseFirstTimeline() -> None:
        method = "Pixera.Compound.pauseFirstTimeline"
        params = []
        return [method, params, []]

    @staticmethod
    def stopFirstTimeline() -> None:
        method = "Pixera.Compound.stopFirstTimeline"
        params = []
        return [method, params, []]

    @staticmethod
    def setOpacityOnTimeline(timelineName: str, opacity: float) -> None:
        method = "Pixera.Compound.setOpacityOnTimeline"
        params = ["timelineName", "opacity"]
        return [method, params, [timelineName, opacity]]

    @staticmethod
    def getOpacityOnTimeline(timelineName: str) -> float:
        method = "Pixera.Compound.getOpacityOnTimeline"
        params = ["timelineName"]
        return [method, params, [timelineName]]

    @staticmethod
    def setPosValue(val: float) -> None:
        method = "Pixera.Compound.setPosValue"
        params = ["val"]
        return [method, params, [val]]

    @staticmethod
    def setPosValueXY(valX: float, valY: float) -> None:
        method = "Pixera.Compound.setPosValueXY"
        params = ["valX", "valY"]
        return [method, params, [valX, valY]]

    @staticmethod
    def setParamValue(path: str, value: float) -> None:
        method = "Pixera.Compound.setParamValue"
        params = ["path", "value"]
        return [method, params, [path, value]]

    @staticmethod
    def applyCueAtIndexOnTimelineAtIndex(cueIndex: int, timelineIndex: int, blendDuration: Optional[float]) -> None:
        method = "Pixera.Compound.applyCueAtIndexOnTimelineAtIndex"
        params = ["cueIndex", "timelineIndex", "blendDuration"]
        return [method, params, [cueIndex, timelineIndex, blendDuration]]

    @staticmethod
    def applyCueNumberOnTimelineAtIndex(cueNumber: int, timelineIndex: int, blendDuration: Optional[float]) -> None:
        method = "Pixera.Compound.applyCueNumberOnTimelineAtIndex"
        params = ["cueNumber", "timelineIndex", "blendDuration"]
        return [method, params, [cueNumber, timelineIndex, blendDuration]]

    @staticmethod
    def applyCueNumberOnTimeline(timelineName: str, cueNumber: int, blendDuration: Optional[float]) -> None:
        method = "Pixera.Compound.applyCueNumberOnTimeline"
        params = ["timelineName", "cueNumber", "blendDuration"]
        return [method, params, [timelineName, cueNumber, blendDuration]]

    @staticmethod
    def applyCueOnTimeline(timelineName: str, cueName: str, blendDuration: Optional[float]) -> None:
        method = "Pixera.Compound.applyCueOnTimeline"
        params = ["timelineName", "cueName", "blendDuration"]
        return [method, params, [timelineName, cueName, blendDuration]]

    @staticmethod
    def addResourceToFolder(namePath: str, filePath: str) -> handle:
        method = "Pixera.Compound.addResourceToFolder"
        params = ["namePath", "filePath"]
        return [method, params, [namePath, filePath]]

    @staticmethod
    def assignResourceToLayer(resourcePath: str, layerPath: str) -> None:
        method = "Pixera.Compound.assignResourceToLayer"
        params = ["resourcePath", "layerPath"]
        return [method, params, [resourcePath, layerPath]]

    @staticmethod
    def refreshResource(resourcePath: str) -> None:
        method = "Pixera.Compound.refreshResource"
        params = ["resourcePath"]
        return [method, params, [resourcePath]]

    @staticmethod
    def setTransportModeOnLayer(layerPath: str, mode: int, loop: bool) -> None:
        method = "Pixera.Compound.setTransportModeOnLayer"
        params = ["layerPath", "mode", "loop"]
        return [method, params, [layerPath, mode, loop]]

    @staticmethod
    def getTransportModeOnLayer(layerPath: str) -> int:
        method = "Pixera.Compound.getTransportModeOnLayer"
        params = ["layerPath"]
        return [method, params, [layerPath]]

    @staticmethod
    def getResourceAssignedToLayer(layerPath: str) -> str:
        method = "Pixera.Compound.getResourceAssignedToLayer"
        params = ["layerPath"]
        return [method, params, [layerPath]]

    @staticmethod
    def assignResourceToClipAtTimeByDmxId(layerPath: str, dmxFolderId: int, dmxFileId: int, time: float) -> None:
        method = "Pixera.Compound.assignResourceToClipAtTimeByDmxId"
        params = ["layerPath", "dmxFolderId", "dmxFileId", "time"]
        return [method, params, [layerPath, dmxFolderId, dmxFileId, time]]

    @staticmethod
    def assignResourceToClipAtHMSFStringByDmxId(layerPath: str, dmxFolderId: int, dmxFileId: int, hmsf: str) -> None:
        method = "Pixera.Compound.assignResourceToClipAtHMSFStringByDmxId"
        params = ["layerPath", "dmxFolderId", "dmxFileId", "hmsf"]
        return [method, params, [layerPath, dmxFolderId, dmxFileId, hmsf]]

    @staticmethod
    def assignResourceToClipAtHMSFByDmxId(layerPath: str, dmxFolderId: int, dmxFileId: int, h: int, m: int, s: int, f: int) -> None:
        method = "Pixera.Compound.assignResourceToClipAtHMSFByDmxId"
        params = ["layerPath", "dmxFolderId", "dmxFileId", "h", "m", "s", "f"]
        return [method, params, [layerPath, dmxFolderId, dmxFileId, h, m, s, f]]

    @staticmethod
    def setCurrentTimeOfTimeline(name: str, time: int) -> None:
        method = "Pixera.Compound.setCurrentTimeOfTimeline"
        params = ["name", "time"]
        return [method, params, [name, time]]

    @staticmethod
    def setCurrentTimeOfTimelineInSeconds(name: str, time: float) -> None:
        method = "Pixera.Compound.setCurrentTimeOfTimelineInSeconds"
        params = ["name", "time"]
        return [method, params, [name, time]]

    @staticmethod
    def setCurrentTimeAndTransportModeOfTimelineInSeconds(name: str, time: float, mode: int) -> None:
        method = "Pixera.Compound.setCurrentTimeAndTransportModeOfTimelineInSeconds"
        params = ["name", "time", "mode"]
        return [method, params, [name, time, mode]]

    @staticmethod
    def getFpsOfTimeline(name: str) -> float:
        method = "Pixera.Compound.getFpsOfTimeline"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getCurrentTimeOfTimeline(name: str) -> int:
        method = "Pixera.Compound.getCurrentTimeOfTimeline"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getCurrentTimeOfTimelineInSeconds(name: str) -> float:
        method = "Pixera.Compound.getCurrentTimeOfTimelineInSeconds"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getCurrentHMSFOfTimeline(name: str) -> str:
        method = "Pixera.Compound.getCurrentHMSFOfTimeline"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getCurrentCountdownOfTimeline(name: str) -> int:
        method = "Pixera.Compound.getCurrentCountdownOfTimeline"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getCurrentCountdownHMSFOfTimeline(name: str) -> str:
        method = "Pixera.Compound.getCurrentCountdownHMSFOfTimeline"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def blockUiTimelineUpdates(doBlock: bool, terminationDurationInMs: Optional[int]) -> None:
        method = "Pixera.Compound.blockUiTimelineUpdates"
        params = ["doBlock", "terminationDurationInMs"]
        return [method, params, [doBlock, terminationDurationInMs]]

    @staticmethod
    def startOpacityAnimationOfTimeline(name: str, fadeIn: bool, fullFadeDuration: float) -> None:
        method = "Pixera.Compound.startOpacityAnimationOfTimeline"
        params = ["name", "fadeIn", "fullFadeDuration"]
        return [method, params, [name, fadeIn, fullFadeDuration]]

    @staticmethod
    def createClipOnLayerAtTimeWithResource(layerPath: str, time: float, resourcePath: str) -> None:
        method = "Pixera.Compound.createClipOnLayerAtTimeWithResource"
        params = ["layerPath", "time", "resourcePath"]
        return [method, params, [layerPath, time, resourcePath]]

    @staticmethod
    def removeClipOnLayerWithIndex(layerPath: str, clipIndex: int) -> None:
        method = "Pixera.Compound.removeClipOnLayerWithIndex"
        params = ["layerPath", "clipIndex"]
        return [method, params, [layerPath, clipIndex]]

    @staticmethod
    def removeAllClipsOnLayer(layerPath: str) -> None:
        method = "Pixera.Compound.removeAllClipsOnLayer"
        params = ["layerPath"]
        return [method, params, [layerPath]]

    @staticmethod
    def getClipDurationInSecondsWithIndex(layerPath: str, clipIndex: int) -> float:
        method = "Pixera.Compound.getClipDurationInSecondsWithIndex"
        params = ["layerPath", "clipIndex"]
        return [method, params, [layerPath, clipIndex]]

    @staticmethod
    def getClipDurationInFramesWithIndex(layerPath: str, clipIndex: int) -> int:
        method = "Pixera.Compound.getClipDurationInFramesWithIndex"
        params = ["layerPath", "clipIndex"]
        return [method, params, [layerPath, clipIndex]]

    @staticmethod
    def getClipTimeInSecondsWithIndex(layerPath: str, clipIndex: int) -> float:
        method = "Pixera.Compound.getClipTimeInSecondsWithIndex"
        params = ["layerPath", "clipIndex"]
        return [method, params, [layerPath, clipIndex]]

    @staticmethod
    def getClipEndTimeInSecondsWithIndex(layerPath: str, clipIndex: int) -> float:
        method = "Pixera.Compound.getClipEndTimeInSecondsWithIndex"
        params = ["layerPath", "clipIndex"]
        return [method, params, [layerPath, clipIndex]]

    @staticmethod
    def getResourceDurationInSeconds(resourcePath: str) -> float:
        method = "Pixera.Compound.getResourceDurationInSeconds"
        params = ["resourcePath"]
        return [method, params, [resourcePath]]

    @staticmethod
    def getParamValue(path: str) -> float:
        method = "Pixera.Compound.getParamValue"
        params = ["path"]
        return [method, params, [path]]

    @staticmethod
    def setTimecodeInput(hour: int, minute: int, second: int, frame: int, elapsedTime: float, running: bool, freshMode: int, stateToken: int, format: int) -> float:
        method = "Pixera.Compound.setTimecodeInput"
        params = ["hour", "minute", "second", "frame", "elapsedTime", "running", "freshMode", "stateToken", "format"]
        return [method, params, [hour, minute, second, frame, elapsedTime, running, freshMode, stateToken, format]]

    @staticmethod
    def takeOverAllClients() -> None:
        method = "Pixera.Compound.takeOverAllClients"
        params = []
        return [method, params, []]

    @staticmethod
    def setPauseSmpteInput(doPause: bool) -> None:
        method = "Pixera.Compound.setPauseSmpteInput"
        params = ["doPause"]
        return [method, params, [doPause]]

    @staticmethod
    def closeApp(saveProject: bool) -> None:
        method = "Pixera.Session.closeApp"
        params = ["saveProject"]
        return [method, params, [saveProject]]

    @staticmethod
    def loadProject(path: str) -> None:
        method = "Pixera.Session.loadProject"
        params = ["path"]
        return [method, params, [path]]

    @staticmethod
    def saveProject() -> None:
        method = "Pixera.Session.saveProject"
        params = []
        return [method, params, []]

    @staticmethod
    def saveProjectAs(path: str) -> None:
        method = "Pixera.Session.saveProjectAs"
        params = ["path"]
        return [method, params, [path]]

    @staticmethod
    def getProjectName() -> str:
        method = "Pixera.Session.getProjectName"
        params = []
        return [method, params, []]

    @staticmethod
    def setProjectName(name: str) -> None:
        method = "Pixera.Session.setProjectName"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getProjectDirectory() -> str:
        method = "Pixera.Session.getProjectDirectory"
        params = []
        return [method, params, []]

    @staticmethod
    def getControlMultiUserSessionName() -> str:
        method = "Pixera.Session.getControlMultiUserSessionName"
        params = []
        return [method, params, []]

    @staticmethod
    def shutdownSystem(mode: Optional[int]) -> None:
        method = "Pixera.Session.shutdownSystem"
        params = ["mode"]
        return [method, params, [mode]]

    @staticmethod
    def getLiveSystemIps() -> List[str]:
        method = "Pixera.Session.getLiveSystemIps"
        params = []
        return [method, params, []]

    @staticmethod
    def getLiveSystemState(ip: str) -> str:
        method = "Pixera.Session.getLiveSystemState"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def liveSystemStateChange(ip: str, state: str) -> None:
        method = "Pixera.Session.liveSystemStateChange"
        params = ["ip", "state"]
        return [method, params, [ip, state]]

    @staticmethod
    def shutdownLiveSystem(ip: str, mode: Optional[int]) -> None:
        method = "Pixera.Session.shutdownLiveSystem"
        params = ["ip", "mode"]
        return [method, params, [ip, mode]]

    @staticmethod
    def wakeLiveSystem(ip: str) -> str:
        method = "Pixera.Session.wakeLiveSystem"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def getLiveSystemMacAddress(ip: str) -> str:
        method = "Pixera.Session.getLiveSystemMacAddress"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def startLiveSystem(ip: str) -> None:
        method = "Pixera.Session.startLiveSystem"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def startLiveSystems() -> None:
        method = "Pixera.Session.startLiveSystems"
        params = []
        return [method, params, []]

    @staticmethod
    def stopLiveSystem(ip: str) -> None:
        method = "Pixera.Session.stopLiveSystem"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def stopLiveSystems() -> None:
        method = "Pixera.Session.stopLiveSystems"
        params = []
        return [method, params, []]

    @staticmethod
    def restartLiveSystem(ip: str) -> None:
        method = "Pixera.Session.restartLiveSystem"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def restartLiveSystems() -> None:
        method = "Pixera.Session.restartLiveSystems"
        params = []
        return [method, params, []]

    @staticmethod
    def remoteSystemStateChange(ip: str, state: str) -> None:
        method = "Pixera.Session.remoteSystemStateChange"
        params = ["ip", "state"]
        return [method, params, [ip, state]]

    @staticmethod
    def getRemoteSystemIps() -> List[str]:
        method = "Pixera.Session.getRemoteSystemIps"
        params = []
        return [method, params, []]

    @staticmethod
    def getRemoteSystemState(ip: str) -> str:
        method = "Pixera.Session.getRemoteSystemState"
        params = ["ip"]
        return [method, params, [ip]]

    @staticmethod
    def setVideoStreamActiveState(ip: str, device: str, isActive: bool) -> None:
        method = "Pixera.Session.setVideoStreamActiveState"
        params = ["ip", "device", "isActive"]
        return [method, params, [ip, device, isActive]]

    @staticmethod
    def getVideoStreamActiveState(ip: str, device: str) -> bool:
        method = "Pixera.Session.getVideoStreamActiveState"
        params = ["ip", "device"]
        return [method, params, [ip, device]]

    @staticmethod
    def getDefaultClipDurationsAsJsonString() -> str:
        method = "Pixera.Session.getDefaultClipDurationsAsJsonString"
        params = []
        return [method, params, []]

    @staticmethod
    def getLiveSystems() -> List[handle]:
        method = "Pixera.LiveSystems.getLiveSystems"
        params = []
        return [method, params, []]

    @staticmethod
    def liveSystemNotAvailable(reason: int, system: handle) -> None:
        method = "Pixera.LiveSystems.liveSystemNotAvailable"
        params = ["reason", "system"]
        return [method, params, [reason, system]]

    @staticmethod
    def getMultiUserMembers() -> List[handle]:
        method = "Pixera.LiveSystems.getMultiUserMembers"
        params = []
        return [method, params, []]

    @staticmethod
    def getUsagePresets() -> List[handle]:
        method = "Pixera.LiveSystems.getUsagePresets"
        params = []
        return [method, params, []]

    class MultiUserMember:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIp(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getIp"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getState(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getState"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getPerformanceMonitoringValuesJson(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getPerformanceMonitoringValuesJson"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getPerformanceMonitoringValuesJsonEx(handle: handle, filter: str) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getPerformanceMonitoringValuesJsonEx"
            params = ["handle, filter"]

            return [method, params, [handle, filter]]

        @staticmethod
        def resetCumulativePerformanceMonitoringValues(handle: handle) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.resetCumulativePerformanceMonitoringValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def ensureFileDistribution(handle: handle, includeNotUsedYet: bool) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.ensureFileDistribution"
            params = ["handle, includeNotUsedYet"]

            return [method, params, [handle, includeNotUsedYet]]

        @staticmethod
        def shutDown(handle: handle, mode: int) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.shutDown"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def wakeUp(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.wakeUp"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getMacAddress(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getMacAddress"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.resetEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def restartEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.restartEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def startEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.startEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def closeEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.closeEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def triggerBackup(handle: handle, applyControlCommand: Optional[bool]) -> None:
            method = "Pixera.LiveSystems.MultiUserMember.triggerBackup"
            params = ["handle, applyControlCommand"]

            return [method, params, [handle, applyControlCommand]]

        @staticmethod
        def getStructureJson(handle: handle) -> str:
            method = "Pixera.LiveSystems.MultiUserMember.getStructureJson"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.LiveSystems.MultiUserMember.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

    class LiveSystem:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIp(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getIp"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getState(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getState"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setBackupRole(handle: handle, role: int) -> None:
            method = "Pixera.LiveSystems.LiveSystem.setBackupRole"
            params = ["handle, role"]

            return [method, params, [handle, role]]

        @staticmethod
        def getBackupRole(handle: handle) -> int:
            method = "Pixera.LiveSystems.LiveSystem.getBackupRole"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getPerformanceMonitoringValuesJson(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getPerformanceMonitoringValuesJson"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getPerformanceMonitoringValuesJsonEx(handle: handle, filter: str) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getPerformanceMonitoringValuesJsonEx"
            params = ["handle, filter"]

            return [method, params, [handle, filter]]

        @staticmethod
        def resetCumulativePerformanceMonitoringValues(handle: handle) -> None:
            method = "Pixera.LiveSystems.LiveSystem.resetCumulativePerformanceMonitoringValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def moveMappingsToOutputs(handle: handle, hdlSrc: handle, outputIdPathMapStr: str) -> None:
            method = "Pixera.LiveSystems.LiveSystem.moveMappingsToOutputs"
            params = ["handle, hdlSrc, outputIdPathMapStr"]

            return [method, params, [handle, hdlSrc, outputIdPathMapStr]]

        @staticmethod
        def setUsagePresetName(handle: handle, name: str) -> None:
            method = "Pixera.LiveSystems.LiveSystem.setUsagePresetName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getUsagePresetName(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getUsagePresetName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def updateUsagePreset(handle: handle) -> None:
            method = "Pixera.LiveSystems.LiveSystem.updateUsagePreset"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def saveUsagePresetAs(handle: handle, name: str) -> None:
            method = "Pixera.LiveSystems.LiveSystem.saveUsagePresetAs"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def applyUsagePreset(handle: handle, name: str) -> None:
            method = "Pixera.LiveSystems.LiveSystem.applyUsagePreset"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def exportUsagePreset(handle: handle, path: str) -> None:
            method = "Pixera.LiveSystems.LiveSystem.exportUsagePreset"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def importUsagePreset(handle: handle, path: str) -> None:
            method = "Pixera.LiveSystems.LiveSystem.importUsagePreset"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def ensureFileDistribution(handle: handle, includeNotUsedYet: bool) -> None:
            method = "Pixera.LiveSystems.LiveSystem.ensureFileDistribution"
            params = ["handle, includeNotUsedYet"]

            return [method, params, [handle, includeNotUsedYet]]

        @staticmethod
        def shutDown(handle: handle, mode: int) -> None:
            method = "Pixera.LiveSystems.LiveSystem.shutDown"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def wakeUp(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.wakeUp"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getMacAddress(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getMacAddress"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getGraphicsDevices(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.LiveSystem.getGraphicsDevices"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getEnabledOutputs(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.LiveSystem.getEnabledOutputs"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getAllOutputs(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.LiveSystem.getAllOutputs"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getVideoStreamOutputs(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.LiveSystem.getVideoStreamOutputs"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.LiveSystem.resetEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def restartEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.LiveSystem.restartEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def startEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.LiveSystem.startEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def closeEngine(handle: handle) -> None:
            method = "Pixera.LiveSystems.LiveSystem.closeEngine"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setAudioMasterVolume(handle: handle, channel: int, volume: float) -> None:
            method = "Pixera.LiveSystems.LiveSystem.setAudioMasterVolume"
            params = ["handle, channel, volume"]

            return [method, params, [handle, channel, volume]]

        @staticmethod
        def getAudioMasterVolume(handle: handle, channel: int) -> float:
            method = "Pixera.LiveSystems.LiveSystem.getAudioMasterVolume"
            params = ["handle, channel"]

            return [method, params, [handle, channel]]

        @staticmethod
        def setAudioMasterMute(handle: handle, channel: int, state: bool) -> None:
            method = "Pixera.LiveSystems.LiveSystem.setAudioMasterMute"
            params = ["handle, channel, state"]

            return [method, params, [handle, channel, state]]

        @staticmethod
        def getAudioMasterMute(handle: handle, channel: int) -> bool:
            method = "Pixera.LiveSystems.LiveSystem.getAudioMasterMute"
            params = ["handle, channel"]

            return [method, params, [handle, channel]]

        @staticmethod
        def toggleAudioMasterMute(handle: handle, channel: int) -> None:
            method = "Pixera.LiveSystems.LiveSystem.toggleAudioMasterMute"
            params = ["handle, channel"]

            return [method, params, [handle, channel]]

        @staticmethod
        def setAudioTimecodeInput(handle: handle, channel: int, state: bool) -> None:
            method = "Pixera.LiveSystems.LiveSystem.setAudioTimecodeInput"
            params = ["handle, channel, state"]

            return [method, params, [handle, channel, state]]

        @staticmethod
        def triggerBackup(handle: handle, applyControlCommand: Optional[bool]) -> None:
            method = "Pixera.LiveSystems.LiveSystem.triggerBackup"
            params = ["handle, applyControlCommand"]

            return [method, params, [handle, applyControlCommand]]

        @staticmethod
        def getStructureJson(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getStructureJson"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.LiveSystems.LiveSystem.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.LiveSystems.LiveSystem.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class UsagePreset:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.LiveSystems.UsagePreset.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def update(handle: handle) -> None:
            method = "Pixera.LiveSystems.UsagePreset.update"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def apply(handle: handle, destinationIp: str) -> None:
            method = "Pixera.LiveSystems.UsagePreset.apply"
            params = ["handle, destinationIp"]

            return [method, params, [handle, destinationIp]]

        @staticmethod
        def importFromFile(handle: handle, path: str) -> None:
            method = "Pixera.LiveSystems.UsagePreset.importFromFile"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def exportToFile(handle: handle, path: str) -> None:
            method = "Pixera.LiveSystems.UsagePreset.exportToFile"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.LiveSystems.UsagePreset.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.LiveSystems.UsagePreset.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class GraphicsDevice:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.LiveSystems.GraphicsDevice.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getEnabledOutputs(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.GraphicsDevice.getEnabledOutputs"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getAllOutputs(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.GraphicsDevice.getAllOutputs"
            params = ["handle"]

            return [method, params, [handle]]

    class Output:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.LiveSystems.Output.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setActive(handle: handle, active: bool) -> None:
            method = "Pixera.LiveSystems.Output.setActive"
            params = ["handle, active"]

            return [method, params, [handle, active]]

        @staticmethod
        def getActive(handle: handle) -> bool:
            method = "Pixera.LiveSystems.Output.getActive"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setIdentify(handle: handle, state: bool) -> None:
            method = "Pixera.LiveSystems.Output.setIdentify"
            params = ["handle, state"]

            return [method, params, [handle, state]]

        @staticmethod
        def getIdentify(handle: handle) -> bool:
            method = "Pixera.LiveSystems.Output.getIdentify"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getAssignedScreens(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.Output.getAssignedScreens"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getAssignedProjectors(handle: handle) -> List[handle]:
            method = "Pixera.LiveSystems.Output.getAssignedProjectors"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getEnabled(handle: handle) -> bool:
            method = "Pixera.LiveSystems.Output.getEnabled"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getForPreview(handle: handle) -> bool:
            method = "Pixera.LiveSystems.Output.getForPreview"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setIsOutputAggregate(handle: handle, state: bool) -> None:
            method = "Pixera.LiveSystems.Output.setIsOutputAggregate"
            params = ["handle, state"]

            return [method, params, [handle, state]]

        @staticmethod
        def getIsOutputAggregate(handle: handle) -> bool:
            method = "Pixera.LiveSystems.Output.getIsOutputAggregate"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setAggregateDims(handle: handle, horizontalCount: int, verticalCount: int) -> None:
            method = "Pixera.LiveSystems.Output.setAggregateDims"
            params = ["handle, horizontalCount, verticalCount"]

            return [method, params, [handle, horizontalCount, verticalCount]]

        @staticmethod
        def getAggregateDims(handle: handle) -> List[int]:
            method = "Pixera.LiveSystems.Output.getAggregateDims"
            params = ["handle"]

            return [method, params, [handle]]

    class VideoStream:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.LiveSystems.VideoStream.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setActive(handle: handle, active: bool) -> None:
            method = "Pixera.LiveSystems.VideoStream.setActive"
            params = ["handle, active"]

            return [method, params, [handle, active]]

        @staticmethod
        def getActive(handle: handle) -> bool:
            method = "Pixera.LiveSystems.VideoStream.getActive"
            params = ["handle"]

            return [method, params, [handle]]

    @staticmethod
    def getShowDimsInPixels() -> bool:
        method = "Pixera.Settings.SettingsGeneral.getShowDimsInPixels"
        params = []
        return [method, params, []]

    @staticmethod
    def getShowScaleAsSize() -> bool:
        method = "Pixera.Settings.SettingsGeneral.getShowScaleAsSize"
        params = []
        return [method, params, []]

    @staticmethod
    def setFadeToTimeDelay(timeInMilliseconds: int) -> None:
        method = "Pixera.Settings.SettingsGeneral.setFadeToTimeDelay"
        params = ["timeInMilliseconds"]
        return [method, params, [timeInMilliseconds]]

    @staticmethod
    def getFadeToTimeDelay() -> int:
        method = "Pixera.Settings.SettingsGeneral.getFadeToTimeDelay"
        params = []
        return [method, params, []]

    @staticmethod
    def getTranscodingPresets() -> List[str]:
        method = "Pixera.Settings.SettingsTranscoding.getTranscodingPresets"
        params = []
        return [method, params, []]

    @staticmethod
    def addOrChangeTranscodingPreset(preset: str) -> None:
        method = "Pixera.Settings.SettingsTranscoding.addOrChangeTranscodingPreset"
        params = ["preset"]
        return [method, params, [preset]]

    @staticmethod
    def getScreenWithName(name: str) -> handle:
        method = "Pixera.Screens.getScreenWithName"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def setNamedScreenPosition(name: str, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> None:
        method = "Pixera.Screens.setNamedScreenPosition"
        params = ["name", "xPos", "yPos", "zPos"]
        return [method, params, [name, xPos, yPos, zPos]]

    @staticmethod
    def getScreens() -> List[handle]:
        method = "Pixera.Screens.getScreens"
        params = []
        return [method, params, []]

    @staticmethod
    def getScreenNames() -> List[str]:
        method = "Pixera.Screens.getScreenNames"
        params = []
        return [method, params, []]

    @staticmethod
    def getFirstTimelineWithHomeScreen(screenName: str) -> handle:
        method = "Pixera.Screens.getFirstTimelineWithHomeScreen"
        params = ["screenName"]
        return [method, params, [screenName]]

    @staticmethod
    def getStudioCameras() -> List[handle]:
        method = "Pixera.Screens.getStudioCameras"
        params = []
        return [method, params, []]

    class Screen:
        @staticmethod
        def getId(handle: handle) -> float:
            method = "Pixera.Screens.Screen.getId"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Screens.Screen.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setPosition(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def getPosition(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getPosition"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setRotation(handle: handle, xRot: Optional[float], yRot: Optional[float], zRot: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setRotation"
            params = ["handle, xRot, yRot, zRot"]

            return [method, params, [handle, xRot, yRot, zRot]]

        @staticmethod
        def getRotation(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getRotation"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setScale(handle: handle, xScale: Optional[float], yScale: Optional[float], zScale: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setScale"
            params = ["handle, xScale, yScale, zScale"]

            return [method, params, [handle, xScale, yScale, zScale]]

        @staticmethod
        def getScale(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getScale"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setPosRot(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float], xRot: Optional[float], yRot: Optional[float], zRot: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPosRot"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot]]

        @staticmethod
        def setPosRotAndPerspectivePos(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float], xRot: Optional[float], yRot: Optional[float], zRot: Optional[float], perspXPos: Optional[float], perspYPos: Optional[float], perspZPos: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPosRotAndPerspectivePos"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, perspXPos, perspYPos, perspZPos"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, perspXPos, perspYPos, perspZPos]]

        @staticmethod
        def setPosRotScale(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float], xRot: Optional[float], yRot: Optional[float], zRot: Optional[float], xScale: Optional[float], yScale: Optional[float], zScale: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPosRotScale"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, xScale, yScale, zScale"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, xScale, yScale, zScale]]

        @staticmethod
        def getPersepective(handle: handle) -> handle:
            method = "Pixera.Screens.Screen.getPersepective"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def snapPerspectiveCornersToScreen(handle: handle, mode: int) -> None:
            method = "Pixera.Screens.Screen.snapPerspectiveCornersToScreen"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def setPerspectivePosition(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPerspectivePosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def setPerspectivePositionWithLookAt(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPerspectivePositionWithLookAt"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def getPerspectivePosition(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getPerspectivePosition"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setPerspectiveRotation(handle: handle, xRot: Optional[float], yRot: Optional[float], zRot: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setPerspectiveRotation"
            params = ["handle, xRot, yRot, zRot"]

            return [method, params, [handle, xRot, yRot, zRot]]

        @staticmethod
        def getPerspectiveRotation(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getPerspectiveRotation"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setCameraPosition(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setCameraPosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def setCameraPositionWithLookAt(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setCameraPositionWithLookAt"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def getCameraPosition(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getCameraPosition"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setCameraRotation(handle: handle, xRot: Optional[float], yRot: Optional[float], zRot: Optional[float]) -> bool:
            method = "Pixera.Screens.Screen.setCameraRotation"
            params = ["handle, xRot, yRot, zRot"]

            return [method, params, [handle, xRot, yRot, zRot]]

        @staticmethod
        def getCameraRotation(handle: handle) -> ScreenPosValues:
            method = "Pixera.Screens.Screen.getCameraRotation"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setContentSamplingFrustumBase(handle: handle, x: float, y: float, width: float, height: float, rotation: float, originScreenId: float) -> None:
            method = "Pixera.Screens.Screen.setContentSamplingFrustumBase"
            params = ["handle, x, y, width, height, rotation, originScreenId"]

            return [method, params, [handle, x, y, width, height, rotation, originScreenId]]

        @staticmethod
        def runCalibration(handle: handle, mode: str, diff: str) -> None:
            method = "Pixera.Screens.Screen.runCalibration"
            params = ["handle, mode, diff"]

            return [method, params, [handle, mode, diff]]

        @staticmethod
        def editCalibration(handle: handle, diff: str) -> None:
            method = "Pixera.Screens.Screen.editCalibration"
            params = ["handle, diff"]

            return [method, params, [handle, diff]]

        @staticmethod
        def resetWarpFile(handle: handle, diff: str) -> None:
            method = "Pixera.Screens.Screen.resetWarpFile"
            params = ["handle, diff"]

            return [method, params, [handle, diff]]

        @staticmethod
        def loadWarpFile(handle: handle, filePath: str) -> None:
            method = "Pixera.Screens.Screen.loadWarpFile"
            params = ["handle, filePath"]

            return [method, params, [handle, filePath]]

        @staticmethod
        def loadWarpFileWithDiff(handle: handle, filePath: str, diff: str) -> None:
            method = "Pixera.Screens.Screen.loadWarpFileWithDiff"
            params = ["handle, filePath, diff"]

            return [method, params, [handle, filePath, diff]]

        @staticmethod
        def addWarpFile(handle: handle, filePath: str) -> None:
            method = "Pixera.Screens.Screen.addWarpFile"
            params = ["handle, filePath"]

            return [method, params, [handle, filePath]]

        @staticmethod
        def addWarpFileWithDiff(handle: handle, filePath: str, diff: str) -> None:
            method = "Pixera.Screens.Screen.addWarpFileWithDiff"
            params = ["handle, filePath, diff"]

            return [method, params, [handle, filePath, diff]]

        @staticmethod
        def loadColorCalibration(handle: handle, calibrationName: str) -> None:
            method = "Pixera.Screens.Screen.loadColorCalibration"
            params = ["handle, calibrationName"]

            return [method, params, [handle, calibrationName]]

        @staticmethod
        def runColorCalibration(handle: handle) -> None:
            method = "Pixera.Screens.Screen.runColorCalibration"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setIsVisible(handle: handle, isVisible: bool) -> None:
            method = "Pixera.Screens.Screen.setIsVisible"
            params = ["handle, isVisible"]

            return [method, params, [handle, isVisible]]

        @staticmethod
        def getIsVisible(handle: handle) -> bool:
            method = "Pixera.Screens.Screen.getIsVisible"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setIsProjectable(handle: handle, isProjectable: bool) -> None:
            method = "Pixera.Screens.Screen.setIsProjectable"
            params = ["handle, isProjectable"]

            return [method, params, [handle, isProjectable]]

        @staticmethod
        def getIsProjectable(handle: handle) -> bool:
            method = "Pixera.Screens.Screen.getIsProjectable"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def triggerRefreshMapping(handle: handle) -> None:
            method = "Pixera.Screens.Screen.triggerRefreshMapping"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetAllColorCorrections(handle: handle) -> None:
            method = "Pixera.Screens.Screen.resetAllColorCorrections"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setColorCorrectionWithPath(handle: handle, path: str, value: float) -> None:
            method = "Pixera.Screens.Screen.setColorCorrectionWithPath"
            params = ["handle, path, value"]

            return [method, params, [handle, path, value]]

        @staticmethod
        def getColorCorrectionWithPath(handle: handle, path: str) -> float:
            method = "Pixera.Screens.Screen.getColorCorrectionWithPath"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def setColorCorrectionAsJsonString(handle: handle, colorCorrection: str) -> None:
            method = "Pixera.Screens.Screen.setColorCorrectionAsJsonString"
            params = ["handle, colorCorrection"]

            return [method, params, [handle, colorCorrection]]

        @staticmethod
        def getColorCorrectionAsJsonString(handle: handle) -> str:
            method = "Pixera.Screens.Screen.getColorCorrectionAsJsonString"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getOutput(handle: handle) -> List[handle]:
            method = "Pixera.Screens.Screen.getOutput"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setBlackout(handle: handle, isActive: bool) -> None:
            method = "Pixera.Screens.Screen.setBlackout"
            params = ["handle, isActive"]

            return [method, params, [handle, isActive]]

        @staticmethod
        def getBlackout(handle: handle) -> bool:
            method = "Pixera.Screens.Screen.getBlackout"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Screens.Screen.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Screens.Screen.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Screens.Screen.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class StudioCamera:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Screens.StudioCamera.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setPosition(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> None:
            method = "Pixera.Screens.StudioCamera.setPosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def getPosition(handle: handle, xPos: float, yPos: float, zPos: float) -> List[float]:
            method = "Pixera.Screens.StudioCamera.getPosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def setRotation(handle: handle, xRot: Optional[float], yRot: Optional[float], zRot: Optional[float]) -> None:
            method = "Pixera.Screens.StudioCamera.setRotation"
            params = ["handle, xRot, yRot, zRot"]

            return [method, params, [handle, xRot, yRot, zRot]]

        @staticmethod
        def getRotation(handle: handle, xPos: float, yPos: float, zPos: float) -> List[float]:
            method = "Pixera.Screens.StudioCamera.getRotation"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def setTransformation(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float], xRot: Optional[float], yRot: Optional[float], zRot: Optional[float], fov: Optional[float], aspectRatio: Optional[float]) -> None:
            method = "Pixera.Screens.StudioCamera.setTransformation"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio]]

        @staticmethod
        def setTransformationAndLensProps(handle: handle, xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, iris: float, k1: float, k2: float, centerX: float, centerY: float, panelWidth: float) -> None:
            method = "Pixera.Screens.StudioCamera.setTransformationAndLensProps"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth]]

        @staticmethod
        def setTransformationAndLensPropsExt(handle: handle, xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, focalDistance: float, zoom: float, iris: float, k1: float, k2: float, k3: float, p1: float, p2: float, centerX: float, centerY: float, panelWidth: float, overscan: float) -> None:
            method = "Pixera.Screens.StudioCamera.setTransformationAndLensPropsExt"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, focalDistance, zoom, iris, k1, k2, k3, p1, p2, centerX, centerY, panelWidth, overscan"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, focalDistance, zoom, iris, k1, k2, k3, p1, p2, centerX, centerY, panelWidth, overscan]]

        @staticmethod
        def setTrackingInputPause(handle: handle, pause: bool) -> None:
            method = "Pixera.Screens.StudioCamera.setTrackingInputPause"
            params = ["handle, pause"]

            return [method, params, [handle, pause]]

        @staticmethod
        def getTrackingInputPause(handle: handle) -> bool:
            method = "Pixera.Screens.StudioCamera.getTrackingInputPause"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setUsePositionPropertiesFromTracking(handle: handle, pause: bool) -> None:
            method = "Pixera.Screens.StudioCamera.setUsePositionPropertiesFromTracking"
            params = ["handle, pause"]

            return [method, params, [handle, pause]]

        @staticmethod
        def getUsePositionPropertiesFromTracking(handle: handle) -> bool:
            method = "Pixera.Screens.StudioCamera.getUsePositionPropertiesFromTracking"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setUseRotationPropertiesFromTracking(handle: handle, pause: bool) -> None:
            method = "Pixera.Screens.StudioCamera.setUseRotationPropertiesFromTracking"
            params = ["handle, pause"]

            return [method, params, [handle, pause]]

        @staticmethod
        def getUseRotationPropertiesFromTracking(handle: handle) -> bool:
            method = "Pixera.Screens.StudioCamera.getUseRotationPropertiesFromTracking"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Screens.StudioCamera.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Screens.StudioCamera.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Screens.StudioCamera.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class Perspective:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Screens.Perspective.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTransformation(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float], xRot: Optional[float], yRot: Optional[float], zRot: Optional[float], fov: Optional[float], aspectRatio: Optional[float], lockLookAtPt: Optional[bool]) -> None:
            method = "Pixera.Screens.Perspective.setTransformation"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, lockLookAtPt"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, lockLookAtPt]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Screens.Perspective.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Screens.Perspective.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Screens.Perspective.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    @staticmethod
    def getProjectorWithName(name: str) -> handle:
        method = "Pixera.Projectors.getProjectorWithName"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getProjectors() -> List[handle]:
        method = "Pixera.Projectors.getProjectors"
        params = []
        return [method, params, []]

    @staticmethod
    def getProjectorNames() -> List[str]:
        method = "Pixera.Projectors.getProjectorNames"
        params = []
        return [method, params, []]

    class Projector:
        @staticmethod
        def getPosition(handle: handle) -> ProjectorPosValues:
            method = "Pixera.Projectors.Projector.getPosition"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setPosition(handle: handle, xPos: Optional[float], yPos: Optional[float], zPos: Optional[float]) -> bool:
            method = "Pixera.Projectors.Projector.setPosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def getRotation(handle: handle) -> ProjectorPosValues:
            method = "Pixera.Projectors.Projector.getRotation"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setRotation(handle: handle, xRot: Optional[float], yRot: Optional[float], zRot: Optional[float]) -> bool:
            method = "Pixera.Projectors.Projector.setRotation"
            params = ["handle, xRot, yRot, zRot"]

            return [method, params, [handle, xRot, yRot, zRot]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Projectors.Projector.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def activateScreenMapping(handle: handle, screenId: float, isActive: bool) -> None:
            method = "Pixera.Projectors.Projector.activateScreenMapping"
            params = ["handle, screenId, isActive"]

            return [method, params, [handle, screenId, isActive]]

        @staticmethod
        def setBlackout(handle: handle, isActive: bool) -> None:
            method = "Pixera.Projectors.Projector.setBlackout"
            params = ["handle, isActive"]

            return [method, params, [handle, isActive]]

        @staticmethod
        def getBlackout(handle: handle) -> bool:
            method = "Pixera.Projectors.Projector.getBlackout"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setSoftedgeVisible(handle: handle, screenName: str, visible: bool) -> None:
            method = "Pixera.Projectors.Projector.setSoftedgeVisible"
            params = ["handle, screenName, visible"]

            return [method, params, [handle, screenName, visible]]

        @staticmethod
        def resetAllColorCorrections(handle: handle) -> None:
            method = "Pixera.Projectors.Projector.resetAllColorCorrections"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setColorCorrectionWithPath(handle: handle, path: str, value: float) -> None:
            method = "Pixera.Projectors.Projector.setColorCorrectionWithPath"
            params = ["handle, path, value"]

            return [method, params, [handle, path, value]]

        @staticmethod
        def getColorCorrectionWithPath(handle: handle, path: str) -> float:
            method = "Pixera.Projectors.Projector.getColorCorrectionWithPath"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def setColorCorrectionAsJsonString(handle: handle, colorCorrection: str) -> None:
            method = "Pixera.Projectors.Projector.setColorCorrectionAsJsonString"
            params = ["handle, colorCorrection"]

            return [method, params, [handle, colorCorrection]]

        @staticmethod
        def getColorCorrectionAsJsonString(handle: handle) -> str:
            method = "Pixera.Projectors.Projector.getColorCorrectionAsJsonString"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getOutput(handle: handle, index: Optional[int]) -> handle:
            method = "Pixera.Projectors.Projector.getOutput"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def setOutput(handle: handle, outputHandle: handle) -> None:
            method = "Pixera.Projectors.Projector.setOutput"
            params = ["handle, outputHandle"]

            return [method, params, [handle, outputHandle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Projectors.Projector.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Projectors.Projector.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Projectors.Projector.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    @staticmethod
    def getResources() -> List[handle]:
        method = "Pixera.Resources.getResources"
        params = []
        return [method, params, []]

    @staticmethod
    def getResourceFolderWithNamePath(namePath: str) -> handle:
        method = "Pixera.Resources.getResourceFolderWithNamePath"
        params = ["namePath"]
        return [method, params, [namePath]]

    @staticmethod
    def getResourceFolders() -> List[handle]:
        method = "Pixera.Resources.getResourceFolders"
        params = []
        return [method, params, []]

    @staticmethod
    def getTranscodingFolders() -> List[handle]:
        method = "Pixera.Resources.getTranscodingFolders"
        params = []
        return [method, params, []]

    @staticmethod
    def getJsonDescrip() -> str:
        method = "Pixera.Resources.getJsonDescrip"
        params = []
        return [method, params, []]

    class ResourceFolder:
        @staticmethod
        def ref(handle: handle) -> handle:
            method = "Pixera.Resources.ResourceFolder.ref"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Resources.ResourceFolder.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setName(handle: handle, name: str) -> None:
            method = "Pixera.Resources.ResourceFolder.setName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getResourceFolders(handle: handle) -> List[handle]:
            method = "Pixera.Resources.ResourceFolder.getResourceFolders"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getResources(handle: handle) -> List[handle]:
            method = "Pixera.Resources.ResourceFolder.getResources"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getResourceAtIndex(handle: handle, index: int) -> handle:
            method = "Pixera.Resources.ResourceFolder.getResourceAtIndex"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def addResource(handle: handle, path: str) -> handle:
            method = "Pixera.Resources.ResourceFolder.addResource"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def addResourcesFromDirectory(handle: handle, path: str, removeOthers: bool, checkRedundancy: bool) -> List[handle]:
            method = "Pixera.Resources.ResourceFolder.addResourcesFromDirectory"
            params = ["handle, path, removeOthers, checkRedundancy"]

            return [method, params, [handle, path, removeOthers, checkRedundancy]]

        @staticmethod
        def addResourcesFromDirectoryRemoveAssets(handle: handle, path: str, removeOthers: bool, checkRedundancy: bool) -> List[handle]:
            method = "Pixera.Resources.ResourceFolder.addResourcesFromDirectoryRemoveAssets"
            params = ["handle, path, removeOthers, checkRedundancy"]

            return [method, params, [handle, path, removeOthers, checkRedundancy]]

        @staticmethod
        def addInternalResource(handle: handle, signature: str, resKind: int) -> handle:
            method = "Pixera.Resources.ResourceFolder.addInternalResource"
            params = ["handle, signature, resKind"]

            return [method, params, [handle, signature, resKind]]

        @staticmethod
        def createFoldersFrom(handle: handle, path: str) -> None:
            method = "Pixera.Resources.ResourceFolder.createFoldersFrom"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def refreshResources(handle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.refreshResources"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def moveResourceToThis(handle: handle, id: float) -> None:
            method = "Pixera.Resources.ResourceFolder.moveResourceToThis"
            params = ["handle, id"]

            return [method, params, [handle, id]]

        @staticmethod
        def removeThis(handle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.removeThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeThisIncludingAssets(handle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.removeThisIncludingAssets"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeAllContents(handle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.removeAllContents"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeAllContentsIncludingAssets(handle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.removeAllContentsIncludingAssets"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def deleteAllContentsAssetsFromLiveSystem(handle: handle, apEntityLiveSystemHandle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.deleteAllContentsAssetsFromLiveSystem"
            params = ["handle, apEntityLiveSystemHandle"]

            return [method, params, [handle, apEntityLiveSystemHandle]]

        @staticmethod
        def resetDistributionTargets(handle: handle) -> None:
            method = "Pixera.Resources.ResourceFolder.resetDistributionTargets"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def changeDistributionTarget(handle: handle, apEntityLiveSystemHandle: handle, shouldDistribute: bool) -> None:
            method = "Pixera.Resources.ResourceFolder.changeDistributionTarget"
            params = ["handle, apEntityLiveSystemHandle, shouldDistribute"]

            return [method, params, [handle, apEntityLiveSystemHandle, shouldDistribute]]

        @staticmethod
        def replaceResourcesByString(handle: handle, searchString: str, replaceString: str, path: str) -> None:
            method = "Pixera.Resources.ResourceFolder.replaceResourcesByString"
            params = ["handle, searchString, replaceString, path"]

            return [method, params, [handle, searchString, replaceString, path]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Resources.ResourceFolder.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Resources.ResourceFolder.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Resources.ResourceFolder.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getDmxId(handle: handle) -> int:
            method = "Pixera.Resources.ResourceFolder.getDmxId"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCombinedDmxId(handle: handle) -> int:
            method = "Pixera.Resources.ResourceFolder.getCombinedDmxId"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setDmxId(handle: handle, id: int) -> None:
            method = "Pixera.Resources.ResourceFolder.setDmxId"
            params = ["handle, id"]

            return [method, params, [handle, id]]

    class TranscodingFolder:
        @staticmethod
        def getUsedTranscodingPreset(handle: handle) -> str:
            method = "Pixera.Resources.TranscodingFolder.getUsedTranscodingPreset"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setUsedTranscodingPreset(handle: handle, preset: str) -> None:
            method = "Pixera.Resources.TranscodingFolder.setUsedTranscodingPreset"
            params = ["handle, preset"]

            return [method, params, [handle, preset]]

        @staticmethod
        def getTranscodeAutomatically(handle: handle) -> bool:
            method = "Pixera.Resources.TranscodingFolder.getTranscodeAutomatically"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTranscodeAutomatically(handle: handle, autoTranscode: bool) -> None:
            method = "Pixera.Resources.TranscodingFolder.setTranscodeAutomatically"
            params = ["handle, autoTranscode"]

            return [method, params, [handle, autoTranscode]]

        @staticmethod
        def getUseRxCacheAsDestination(handle: handle) -> bool:
            method = "Pixera.Resources.TranscodingFolder.getUseRxCacheAsDestination"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setRxCacheAsDestination(handle: handle, useRxCache: bool) -> None:
            method = "Pixera.Resources.TranscodingFolder.setRxCacheAsDestination"
            params = ["handle, useRxCache"]

            return [method, params, [handle, useRxCache]]

        @staticmethod
        def getDestinationDirectory(handle: handle) -> str:
            method = "Pixera.Resources.TranscodingFolder.getDestinationDirectory"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setDestinationDirectory(handle: handle, path: str) -> None:
            method = "Pixera.Resources.TranscodingFolder.setDestinationDirectory"
            params = ["handle, path"]

            return [method, params, [handle, path]]

    class Resource:
        @staticmethod
        def ref(handle: handle) -> handle:
            method = "Pixera.Resources.Resource.ref"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeThis(handle: handle) -> None:
            method = "Pixera.Resources.Resource.removeThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def deleteFilesOnSystems(handle: handle) -> None:
            method = "Pixera.Resources.Resource.deleteFilesOnSystems"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeThisIncludingAssets(handle: handle) -> None:
            method = "Pixera.Resources.Resource.removeThisIncludingAssets"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def deleteAssetFromLiveSystem(handle: handle, apEntityLiveSystemHandle: handle) -> None:
            method = "Pixera.Resources.Resource.deleteAssetFromLiveSystem"
            params = ["handle, apEntityLiveSystemHandle"]

            return [method, params, [handle, apEntityLiveSystemHandle]]

        @staticmethod
        def resetDistributionTargets(handle: handle) -> None:
            method = "Pixera.Resources.Resource.resetDistributionTargets"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def changeDistributionTarget(handle: handle, apEntityLiveSystemHandle: handle, shouldDistribute: bool) -> None:
            method = "Pixera.Resources.Resource.changeDistributionTarget"
            params = ["handle, apEntityLiveSystemHandle, shouldDistribute"]

            return [method, params, [handle, apEntityLiveSystemHandle, shouldDistribute]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setName(handle: handle, name: str) -> None:
            method = "Pixera.Resources.Resource.setName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getFps(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getFps"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getResolution(handle: handle) -> List[float]:
            method = "Pixera.Resources.Resource.getResolution"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsActive(handle: handle) -> bool:
            method = "Pixera.Resources.Resource.getIsActive"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getVideoStreamModes(handle: handle) -> List[str]:
            method = "Pixera.Resources.Resource.getVideoStreamModes"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setVideoStreamMode(handle: handle, index: int) -> None:
            method = "Pixera.Resources.Resource.setVideoStreamMode"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def getId(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getId"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getDuration(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getDuration"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getType(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getType"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setCurrentVersion(handle: handle, version: str) -> None:
            method = "Pixera.Resources.Resource.setCurrentVersion"
            params = ["handle, version"]

            return [method, params, [handle, version]]

        @staticmethod
        def getCurrentVersion(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getCurrentVersion"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getVersions(handle: handle) -> List[str]:
            method = "Pixera.Resources.Resource.getVersions"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getVersionSuffix(handle: handle) -> List[str]:
            method = "Pixera.Resources.Resource.getVersionSuffix"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def rescanVersions(handle: handle) -> None:
            method = "Pixera.Resources.Resource.rescanVersions"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getThumbnailAsBase64(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getThumbnailAsBase64"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getHasPendingTransfer(handle: handle) -> bool:
            method = "Pixera.Resources.Resource.getHasPendingTransfer"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsInUse(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getIsInUse"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLastUsageBeginTime(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getLastUsageBeginTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLastUsageBeginTimeAsString(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getLastUsageBeginTimeAsString"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLastUsageEndTime(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getLastUsageEndTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLastUsageEndTimeAsString(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getLastUsageEndTimeAsString"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getFilePath(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getFilePath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setText(handle: handle, text: str) -> None:
            method = "Pixera.Resources.Resource.setText"
            params = ["handle, text"]

            return [method, params, [handle, text]]

        @staticmethod
        def getText(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getText"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setFontWithName(handle: handle, fontName: str) -> bool:
            method = "Pixera.Resources.Resource.setFontWithName"
            params = ["handle, fontName"]

            return [method, params, [handle, fontName]]

        @staticmethod
        def getFontName(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getFontName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setFontWithPath(handle: handle, fontPath: str) -> bool:
            method = "Pixera.Resources.Resource.setFontWithPath"
            params = ["handle, fontPath"]

            return [method, params, [handle, fontPath]]

        @staticmethod
        def setHorizontalTextAlignment(handle: handle, textAlignment: int) -> bool:
            method = "Pixera.Resources.Resource.setHorizontalTextAlignment"
            params = ["handle, textAlignment"]

            return [method, params, [handle, textAlignment]]

        @staticmethod
        def getHorizontalTextAlignment(handle: handle) -> int:
            method = "Pixera.Resources.Resource.getHorizontalTextAlignment"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setVerticalTextAlignment(handle: handle, textAlignment: int) -> bool:
            method = "Pixera.Resources.Resource.setVerticalTextAlignment"
            params = ["handle, textAlignment"]

            return [method, params, [handle, textAlignment]]

        @staticmethod
        def getVerticalTextAlignment(handle: handle) -> int:
            method = "Pixera.Resources.Resource.getVerticalTextAlignment"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setLineHeight(handle: handle, lineHeight: float) -> bool:
            method = "Pixera.Resources.Resource.setLineHeight"
            params = ["handle, lineHeight"]

            return [method, params, [handle, lineHeight]]

        @staticmethod
        def getLineHeight(handle: handle) -> float:
            method = "Pixera.Resources.Resource.getLineHeight"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getTextMeasurementsWidthAndHeight(handle: handle) -> List[int]:
            method = "Pixera.Resources.Resource.getTextMeasurementsWidthAndHeight"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setUrl(handle: handle, url: str) -> None:
            method = "Pixera.Resources.Resource.setUrl"
            params = ["handle, url"]

            return [method, params, [handle, url]]

        @staticmethod
        def getUrl(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getUrl"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setColorTransformPath(handle: handle, colorTransformPath: str) -> None:
            method = "Pixera.Resources.Resource.setColorTransformPath"
            params = ["handle, colorTransformPath"]

            return [method, params, [handle, colorTransformPath]]

        @staticmethod
        def getColorTransformPath(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getColorTransformPath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def clearColorTransformPath(handle: handle) -> None:
            method = "Pixera.Resources.Resource.clearColorTransformPath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def refresh(handle: handle, text: str) -> None:
            method = "Pixera.Resources.Resource.refresh"
            params = ["handle, text"]

            return [method, params, [handle, text]]

        @staticmethod
        def distribute(handle: handle) -> None:
            method = "Pixera.Resources.Resource.distribute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getDmxId(handle: handle) -> int:
            method = "Pixera.Resources.Resource.getDmxId"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setDmxId(handle: handle, id: int) -> None:
            method = "Pixera.Resources.Resource.setDmxId"
            params = ["handle, id"]

            return [method, params, [handle, id]]

        @staticmethod
        def removeMultiresourceIndex(handle: handle, index: int) -> None:
            method = "Pixera.Resources.Resource.removeMultiresourceIndex"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def addMultiresourceItem(handle: handle, id: float) -> None:
            method = "Pixera.Resources.Resource.addMultiresourceItem"
            params = ["handle, id"]

            return [method, params, [handle, id]]

        @staticmethod
        def getMultiresourceItems(handle: handle) -> List[handle]:
            method = "Pixera.Resources.Resource.getMultiresourceItems"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def replaceMultiresourceItemByIndex(handle: handle, index: int, id: float) -> None:
            method = "Pixera.Resources.Resource.replaceMultiresourceItemByIndex"
            params = ["handle, index, id"]

            return [method, params, [handle, index, id]]

        @staticmethod
        def setMultiresourceResolution(handle: handle, width: int, height: int) -> None:
            method = "Pixera.Resources.Resource.setMultiresourceResolution"
            params = ["handle, width, height"]

            return [method, params, [handle, width, height]]

        @staticmethod
        def setMultiresourceItemSizebyIndex(handle: handle, index: int, width: float, height: float) -> None:
            method = "Pixera.Resources.Resource.setMultiresourceItemSizebyIndex"
            params = ["handle, index, width, height"]

            return [method, params, [handle, index, width, height]]

        @staticmethod
        def setMultiresourceItemPositionbyIndex(handle: handle, index: int, x: float, y: float) -> None:
            method = "Pixera.Resources.Resource.setMultiresourceItemPositionbyIndex"
            params = ["handle, index, x, y"]

            return [method, params, [handle, index, x, y]]

        @staticmethod
        def setUseGradient(handle: handle, useGradient: bool) -> None:
            method = "Pixera.Resources.Resource.setUseGradient"
            params = ["handle, useGradient"]

            return [method, params, [handle, useGradient]]

        @staticmethod
        def getUseGradient(handle: handle) -> bool:
            method = "Pixera.Resources.Resource.getUseGradient"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setColors(handle: handle, argbCols: List[uint], positions: List[float], colNames: List[str], useGradient: Optional[bool]) -> None:
            method = "Pixera.Resources.Resource.setColors"
            params = ["handle, argbCols, positions, colNames, useGradient"]

            return [method, params, [handle, argbCols, positions, colNames, useGradient]]

        @staticmethod
        def setColorAtIndex(handle: handle, index: int, red: int, green: int, blue: int, alpha: int, position: float, name: str, useGradient: Optional[bool]) -> None:
            method = "Pixera.Resources.Resource.setColorAtIndex"
            params = ["handle, index, red, green, blue, alpha, position, name, useGradient"]

            return [method, params, [handle, index, red, green, blue, alpha, position, name, useGradient]]

        @staticmethod
        def getColorAtIndex(handle: handle, colorIndex: int) -> int:
            method = "Pixera.Resources.Resource.getColorAtIndex"
            params = ["handle, colorIndex"]

            return [method, params, [handle, colorIndex]]

        @staticmethod
        def getColorPositionAtIndex(handle: handle, colorIndex: int) -> float:
            method = "Pixera.Resources.Resource.getColorPositionAtIndex"
            params = ["handle, colorIndex"]

            return [method, params, [handle, colorIndex]]

        @staticmethod
        def launchVirtualWorld(handle: handle, action: str) -> None:
            method = "Pixera.Resources.Resource.launchVirtualWorld"
            params = ["handle, action"]

            return [method, params, [handle, action]]

        @staticmethod
        def getUnrealWorld(handle: handle) -> handle:
            method = "Pixera.Resources.Resource.getUnrealWorld"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setMultiResourceItemRestrictedServiceIps(handle: handle, itemIndex: int, ipAdresses: List[str]) -> None:
            method = "Pixera.Resources.Resource.setMultiResourceItemRestrictedServiceIps"
            params = ["handle, itemIndex, ipAdresses"]

            return [method, params, [handle, itemIndex, ipAdresses]]

        @staticmethod
        def getMultiResourceItemRestrictedServiceIps(handle: handle, itemIndex: int) -> List[str]:
            method = "Pixera.Resources.Resource.getMultiResourceItemRestrictedServiceIps"
            params = ["handle, itemIndex"]

            return [method, params, [handle, itemIndex]]

        @staticmethod
        def replace(handle: handle, path: str) -> None:
            method = "Pixera.Resources.Resource.replace"
            params = ["handle, path"]

            return [method, params, [handle, path]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Resources.Resource.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Resources.Resource.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Resources.Resource.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def transcodeWithExisitngPreset(handle: handle, presetName: str, useRxCache: bool, destinationPath: str, startFrame: int, endFrame: int, serviceId: uint) -> None:
            method = "Pixera.Resources.Resource.transcodeWithExisitngPreset"
            params = ["handle, presetName, useRxCache, destinationPath, startFrame, endFrame, serviceId"]

            return [method, params, [handle, presetName, useRxCache, destinationPath, startFrame, endFrame, serviceId]]

        @staticmethod
        def transcodeWithSettings(handle: handle, settings: str, useRxCache: bool, destinationPath: str, startFrame: int, endFrame: int, serviceId: uint) -> None:
            method = "Pixera.Resources.Resource.transcodeWithSettings"
            params = ["handle, settings, useRxCache, destinationPath, startFrame, endFrame, serviceId"]

            return [method, params, [handle, settings, useRxCache, destinationPath, startFrame, endFrame, serviceId]]

        @staticmethod
        def moveToTranscodingFolder(handle: handle, folderPath: str) -> None:
            method = "Pixera.Resources.Resource.moveToTranscodingFolder"
            params = ["handle, folderPath"]

            return [method, params, [handle, folderPath]]

    class UnrealWorld:
        @staticmethod
        def getLevelNames(handle: handle) -> List[str]:
            method = "Pixera.Resources.UnrealWorld.getLevelNames"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def loadLevel(handle: handle, levelName: str) -> None:
            method = "Pixera.Resources.UnrealWorld.loadLevel"
            params = ["handle, levelName"]

            return [method, params, [handle, levelName]]

        @staticmethod
        def getEventTriggerNames(handle: handle) -> List[str]:
            method = "Pixera.Resources.UnrealWorld.getEventTriggerNames"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def triggerEventByName(handle: handle, triggerName: str) -> None:
            method = "Pixera.Resources.UnrealWorld.triggerEventByName"
            params = ["handle, triggerName"]

            return [method, params, [handle, triggerName]]

        @staticmethod
        def createNDisplayConfig(handle: handle) -> None:
            method = "Pixera.Resources.UnrealWorld.createNDisplayConfig"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def runUnreal(handle: handle) -> None:
            method = "Pixera.Resources.UnrealWorld.runUnreal"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def killUnreal(handle: handle) -> None:
            method = "Pixera.Resources.UnrealWorld.killUnreal"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Resources.UnrealWorld.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Resources.UnrealWorld.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Resources.UnrealWorld.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Resources.UnrealWorld.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    @staticmethod
    def getTimelineAtIndex(index: int) -> handle:
        method = "Pixera.Timelines.getTimelineAtIndex"
        params = ["index"]
        return [method, params, [index]]

    @staticmethod
    def getTimelineFromName(name: str) -> handle:
        method = "Pixera.Timelines.getTimelineFromName"
        params = ["name"]
        return [method, params, [name]]

    @staticmethod
    def getTimelines() -> List[handle]:
        method = "Pixera.Timelines.getTimelines"
        params = []
        return [method, params, []]

    @staticmethod
    def getTimelineNames() -> List[str]:
        method = "Pixera.Timelines.getTimelineNames"
        params = []
        return [method, params, []]

    @staticmethod
    def getTimelinesSelected() -> List[handle]:
        method = "Pixera.Timelines.getTimelinesSelected"
        params = []
        return [method, params, []]

    @staticmethod
    def createTimeline() -> handle:
        method = "Pixera.Timelines.createTimeline"
        params = []
        return [method, params, []]

    @staticmethod
    def getNodeFromId(id: float) -> handle:
        method = "Pixera.Timelines.getNodeFromId"
        params = ["id"]
        return [method, params, [id]]

    class Timeline:
        @staticmethod
        def ref(handle: handle) -> handle:
            method = "Pixera.Timelines.Timeline.ref"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeThis(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.removeThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def duplicateThis(handle: handle, withoutClipsCues: Optional[bool]) -> handle:
            method = "Pixera.Timelines.Timeline.duplicateThis"
            params = ["handle, withoutClipsCues"]

            return [method, params, [handle, withoutClipsCues]]

        @staticmethod
        def selectThis(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.selectThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getZoomFactor(handle: handle) -> float:
            method = "Pixera.Timelines.Timeline.getZoomFactor"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setZoomFactor(handle: handle, zoomFactor: float) -> None:
            method = "Pixera.Timelines.Timeline.setZoomFactor"
            params = ["handle, zoomFactor"]

            return [method, params, [handle, zoomFactor]]

        @staticmethod
        def getVerticalScrollOffset(handle: handle) -> int:
            method = "Pixera.Timelines.Timeline.getVerticalScrollOffset"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setVerticalScrollOffset(handle: handle, offset: int) -> None:
            method = "Pixera.Timelines.Timeline.setVerticalScrollOffset"
            params = ["handle, offset"]

            return [method, params, [handle, offset]]

        @staticmethod
        def getHorizontalScrollOffset(handle: handle) -> int:
            method = "Pixera.Timelines.Timeline.getHorizontalScrollOffset"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setHorizontalScrollOffset(handle: handle, offset: int) -> None:
            method = "Pixera.Timelines.Timeline.setHorizontalScrollOffset"
            params = ["handle, offset"]

            return [method, params, [handle, offset]]

        @staticmethod
        def moveInRenderOrder(handle: handle, moveDown: bool) -> None:
            method = "Pixera.Timelines.Timeline.moveInRenderOrder"
            params = ["handle, moveDown"]

            return [method, params, [handle, moveDown]]

        @staticmethod
        def getLayers(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Timeline.getLayers"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLayerNames(handle: handle) -> List[str]:
            method = "Pixera.Timelines.Timeline.getLayerNames"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLayersSelected(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Timeline.getLayersSelected"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def selectLayerByIndex(handle: handle, index: int) -> None:
            method = "Pixera.Timelines.Timeline.selectLayerByIndex"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def selectLayerByNames(handle: handle, layerNames: List[str]) -> None:
            method = "Pixera.Timelines.Timeline.selectLayerByNames"
            params = ["handle, layerNames"]

            return [method, params, [handle, layerNames]]

        @staticmethod
        def getLayerAtIndex(handle: handle, index: int) -> handle:
            method = "Pixera.Timelines.Timeline.getLayerAtIndex"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def createLayer(handle: handle) -> handle:
            method = "Pixera.Timelines.Timeline.createLayer"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCueInfosAsJsonString(handle: handle) -> str:
            method = "Pixera.Timelines.Timeline.getCueInfosAsJsonString"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCues(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Timeline.getCues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCueNames(handle: handle) -> List[str]:
            method = "Pixera.Timelines.Timeline.getCueNames"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCueAtIndex(handle: handle, index: int) -> handle:
            method = "Pixera.Timelines.Timeline.getCueAtIndex"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def getCueFromName(handle: handle, name: str) -> handle:
            method = "Pixera.Timelines.Timeline.getCueFromName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getCueFromNumber(handle: handle, number: int) -> handle:
            method = "Pixera.Timelines.Timeline.getCueFromNumber"
            params = ["handle, number"]

            return [method, params, [handle, number]]

        @staticmethod
        def applyCueWithName(handle: handle, name: str, blendDuration: Optional[float]) -> None:
            method = "Pixera.Timelines.Timeline.applyCueWithName"
            params = ["handle, name, blendDuration"]

            return [method, params, [handle, name, blendDuration]]

        @staticmethod
        def applyCueWithNumber(handle: handle, number: int, blendDuration: Optional[float]) -> None:
            method = "Pixera.Timelines.Timeline.applyCueWithNumber"
            params = ["handle, number, blendDuration"]

            return [method, params, [handle, number, blendDuration]]

        @staticmethod
        def createCue(handle: handle, name: str, timeInFrames: float, operation: int) -> handle:
            method = "Pixera.Timelines.Timeline.createCue"
            params = ["handle, name, timeInFrames, operation"]

            return [method, params, [handle, name, timeInFrames, operation]]

        @staticmethod
        def removeCues(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.removeCues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def createPauseCueBeforeSelectedClips(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.createPauseCueBeforeSelectedClips"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def play(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.play"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def pause(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.pause"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def stop(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.stop"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def toggleTransport(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.toggleTransport"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def store(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.store"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def reset(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.reset"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getAttributes(handle: handle) -> TimelineAttributes:
            method = "Pixera.Timelines.Timeline.getAttributes"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setCurrentFrame(handle: handle, time: int) -> bool:
            method = "Pixera.Timelines.Timeline.setCurrentFrame"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def setCurrentTime(handle: handle, time: int) -> None:
            method = "Pixera.Timelines.Timeline.setCurrentTime"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getCurrentTime(handle: handle) -> int:
            method = "Pixera.Timelines.Timeline.getCurrentTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def scrubCurrentTime(handle: handle, frames: int) -> None:
            method = "Pixera.Timelines.Timeline.scrubCurrentTime"
            params = ["handle, frames"]

            return [method, params, [handle, frames]]

        @staticmethod
        def CurrentTime(handle: handle, time: int, doSet: bool) -> int:
            method = "Pixera.Timelines.Timeline.CurrentTime"
            params = ["handle, time, doSet"]

            return [method, params, [handle, time, doSet]]

        @staticmethod
        def getCurrentHMSF(handle: handle) -> str:
            method = "Pixera.Timelines.Timeline.getCurrentHMSF"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTransportMode(handle: handle, mode: int) -> bool:
            method = "Pixera.Timelines.Timeline.setTransportMode"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def getTransportMode(handle: handle) -> int:
            method = "Pixera.Timelines.Timeline.getTransportMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTimecodeInput(handle: handle, hour: int, minute: int, second: int, frame: int, elapsedTime: float, running: bool, freshMode: int, stateToken: int, format: int) -> float:
            method = "Pixera.Timelines.Timeline.setTimecodeInput"
            params = ["handle, hour, minute, second, frame, elapsedTime, running, freshMode, stateToken, format"]

            return [method, params, [handle, hour, minute, second, frame, elapsedTime, running, freshMode, stateToken, format]]

        @staticmethod
        def getFps(handle: handle) -> float:
            method = "Pixera.Timelines.Timeline.getFps"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Timelines.Timeline.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setName(handle: handle, name: str) -> None:
            method = "Pixera.Timelines.Timeline.setName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def moveToNextCue(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.moveToNextCue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def moveToNextCueIgnoreProperties(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.moveToNextCueIgnoreProperties"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCueNext(handle: handle) -> handle:
            method = "Pixera.Timelines.Timeline.getCueNext"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def moveToPreviousCue(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.moveToPreviousCue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def moveToPreviousCueIgnoreProperties(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.moveToPreviousCueIgnoreProperties"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCuePrevious(handle: handle) -> handle:
            method = "Pixera.Timelines.Timeline.getCuePrevious"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def ignoreNextCue(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.ignoreNextCue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def ignoreNextCueWithOperation(handle: handle, cueOperation: int) -> None:
            method = "Pixera.Timelines.Timeline.ignoreNextCueWithOperation"
            params = ["handle, cueOperation"]

            return [method, params, [handle, cueOperation]]

        @staticmethod
        def blendToTime(handle: handle, goalTime: float, blendDuration: float, preloadDelayInMilliseconds: Optional[int]) -> None:
            method = "Pixera.Timelines.Timeline.blendToTime"
            params = ["handle, goalTime, blendDuration, preloadDelayInMilliseconds"]

            return [method, params, [handle, goalTime, blendDuration, preloadDelayInMilliseconds]]

        @staticmethod
        def blendToTimeWithTransportMode(handle: handle, goalTime: float, blendDuration: float, transportMode: int, preloadDelayInMilliseconds: Optional[int]) -> None:
            method = "Pixera.Timelines.Timeline.blendToTimeWithTransportMode"
            params = ["handle, goalTime, blendDuration, transportMode, preloadDelayInMilliseconds"]

            return [method, params, [handle, goalTime, blendDuration, transportMode, preloadDelayInMilliseconds]]

        @staticmethod
        def setBlendToTimeMode(handle: handle, mode: int) -> bool:
            method = "Pixera.Timelines.Timeline.setBlendToTimeMode"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def setSpeedFactor(handle: handle, factor: float) -> None:
            method = "Pixera.Timelines.Timeline.setSpeedFactor"
            params = ["handle, factor"]

            return [method, params, [handle, factor]]

        @staticmethod
        def getSpeedFactor(handle: handle) -> float:
            method = "Pixera.Timelines.Timeline.getSpeedFactor"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setOpacity(handle: handle, value: float) -> None:
            method = "Pixera.Timelines.Timeline.setOpacity"
            params = ["handle, value"]

            return [method, params, [handle, value]]

        @staticmethod
        def getOpacity(handle: handle) -> float:
            method = "Pixera.Timelines.Timeline.getOpacity"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def startOpacityAnimation(handle: handle, fadeIn: bool, fullFadeDuration: float) -> None:
            method = "Pixera.Timelines.Timeline.startOpacityAnimation"
            params = ["handle, fadeIn, fullFadeDuration"]

            return [method, params, [handle, fadeIn, fullFadeDuration]]

        @staticmethod
        def setSmpteMode(handle: handle, mode: int) -> None:
            method = "Pixera.Timelines.Timeline.setSmpteMode"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def getSmpteMode(handle: handle) -> int:
            method = "Pixera.Timelines.Timeline.getSmpteMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def storeRecordedValues(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.storeRecordedValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setSmpteInputBehaviour(handle: handle, mode: int) -> None:
            method = "Pixera.Timelines.Timeline.setSmpteInputBehaviour"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def getSmpteInputBehaviour(handle: handle) -> int:
            method = "Pixera.Timelines.Timeline.getSmpteInputBehaviour"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setSmpteOffset(handle: handle, time: float) -> None:
            method = "Pixera.Timelines.Timeline.setSmpteOffset"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getSmpteOffset(handle: handle) -> float:
            method = "Pixera.Timelines.Timeline.getSmpteOffset"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetRecordedValues(handle: handle) -> None:
            method = "Pixera.Timelines.Timeline.resetRecordedValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getTimelineInfosAsJsonString(handle: handle) -> str:
            method = "Pixera.Timelines.Timeline.getTimelineInfosAsJsonString"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Timeline.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Timeline.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Timelines.Timeline.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class Layer:
        @staticmethod
        def ref(handle: handle) -> handle:
            method = "Pixera.Timelines.Layer.ref"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeThis(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.removeThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getNodes(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Layer.getNodes"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getNodeWithName(handle: handle, name: str) -> handle:
            method = "Pixera.Timelines.Layer.getNodeWithName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getParamWithName(handle: handle, name: str) -> handle:
            method = "Pixera.Timelines.Layer.getParamWithName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getSpatialParametersAtTime(handle: handle, time: float) -> List[float]:
            method = "Pixera.Timelines.Layer.getSpatialParametersAtTime"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getTimeline(handle: handle) -> handle:
            method = "Pixera.Timelines.Layer.getTimeline"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setName(handle: handle, name: str) -> None:
            method = "Pixera.Timelines.Layer.setName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Timelines.Layer.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetLayer(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.resetLayer"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getLayerJsonDescrip(handle: handle) -> str:
            method = "Pixera.Timelines.Layer.getLayerJsonDescrip"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setLayerJsonDescrip(handle: handle, descrip: str, makeAllDominant: bool) -> None:
            method = "Pixera.Timelines.Layer.setLayerJsonDescrip"
            params = ["handle, descrip, makeAllDominant"]

            return [method, params, [handle, descrip, makeAllDominant]]

        @staticmethod
        def getJsonDescrip(handle: handle) -> str:
            method = "Pixera.Timelines.Layer.getJsonDescrip"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def initFromJsonDescrip(handle: handle, descrip: str) -> None:
            method = "Pixera.Timelines.Layer.initFromJsonDescrip"
            params = ["handle, descrip"]

            return [method, params, [handle, descrip]]

        @staticmethod
        def setOpacity(handle: handle, value: float) -> None:
            method = "Pixera.Timelines.Layer.setOpacity"
            params = ["handle, value"]

            return [method, params, [handle, value]]

        @staticmethod
        def getOpacity(handle: handle) -> float:
            method = "Pixera.Timelines.Layer.getOpacity"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetOpacity(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.resetOpacity"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setVolume(handle: handle, value: float) -> None:
            method = "Pixera.Timelines.Layer.setVolume"
            params = ["handle, value"]

            return [method, params, [handle, value]]

        @staticmethod
        def getVolume(handle: handle) -> float:
            method = "Pixera.Timelines.Layer.getVolume"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetVolume(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.resetVolume"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def muteLayer(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.muteLayer"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def unMuteLayer(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.unMuteLayer"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsLayerMuted(handle: handle) -> bool:
            method = "Pixera.Timelines.Layer.getIsLayerMuted"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def muteAudio(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.muteAudio"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def unMuteAudio(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.unMuteAudio"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsAudioMuted(handle: handle) -> bool:
            method = "Pixera.Timelines.Layer.getIsAudioMuted"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getDmxMuteState(handle: handle) -> int:
            method = "Pixera.Timelines.Layer.getDmxMuteState"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setDmxMuteState(handle: handle, muteState: uint) -> None:
            method = "Pixera.Timelines.Layer.setDmxMuteState"
            params = ["handle, muteState"]

            return [method, params, [handle, muteState]]

        @staticmethod
        def toggleExplicitMute(handle: handle, flag: uint) -> None:
            method = "Pixera.Timelines.Layer.toggleExplicitMute"
            params = ["handle, flag"]

            return [method, params, [handle, flag]]

        @staticmethod
        def setTransport(handle: handle, mode: int, loop: bool) -> None:
            method = "Pixera.Timelines.Layer.setTransport"
            params = ["handle, mode, loop"]

            return [method, params, [handle, mode, loop]]

        @staticmethod
        def getTransportMode(handle: handle) -> int:
            method = "Pixera.Timelines.Layer.getTransportMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetTransportMode(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.resetTransportMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getTransportLoop(handle: handle) -> bool:
            method = "Pixera.Timelines.Layer.getTransportLoop"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def assignResource(handle: handle, id: float) -> None:
            method = "Pixera.Timelines.Layer.assignResource"
            params = ["handle, id"]

            return [method, params, [handle, id]]

        @staticmethod
        def assignResourceWithFade(handle: handle, id: float, fadeDuration: float) -> None:
            method = "Pixera.Timelines.Layer.assignResourceWithFade"
            params = ["handle, id, fadeDuration"]

            return [method, params, [handle, id, fadeDuration]]

        @staticmethod
        def getAssignedResource(handle: handle) -> handle:
            method = "Pixera.Timelines.Layer.getAssignedResource"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetAssignedResource(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.resetAssignedResource"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getAssignedModelResource(handle: handle) -> handle:
            method = "Pixera.Timelines.Layer.getAssignedModelResource"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetAssignedModelResource(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.resetAssignedModelResource"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getFxNames(handle: handle) -> List[str]:
            method = "Pixera.Timelines.Layer.getFxNames"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setFadeDurationDominantResourceChange(handle: handle, value: float) -> None:
            method = "Pixera.Timelines.Layer.setFadeDurationDominantResourceChange"
            params = ["handle, value"]

            return [method, params, [handle, value]]

        @staticmethod
        def getFadeDurationDominantResourceChange(handle: handle) -> float:
            method = "Pixera.Timelines.Layer.getFadeDurationDominantResourceChange"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def createClip(handle: handle) -> handle:
            method = "Pixera.Timelines.Layer.createClip"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def createClipAtTime(handle: handle, timeInFrames: float) -> handle:
            method = "Pixera.Timelines.Layer.createClipAtTime"
            params = ["handle, timeInFrames"]

            return [method, params, [handle, timeInFrames]]

        @staticmethod
        def controlClipBorder(handle: handle, clip: handle, isEnter: bool, isIncremental: bool, entryTime: float) -> None:
            method = "Pixera.Timelines.Layer.controlClipBorder"
            params = ["handle, clip, isEnter, isIncremental, entryTime"]

            return [method, params, [handle, clip, isEnter, isIncremental, entryTime]]

        @staticmethod
        def getClipAtIndex(handle: handle, index: int) -> handle:
            method = "Pixera.Timelines.Layer.getClipAtIndex"
            params = ["handle, index"]

            return [method, params, [handle, index]]

        @staticmethod
        def getClips(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Layer.getClips"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getClipCurrent(handle: handle, offset: int) -> handle:
            method = "Pixera.Timelines.Layer.getClipCurrent"
            params = ["handle, offset"]

            return [method, params, [handle, offset]]

        @staticmethod
        def getClipsSelected(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Layer.getClipsSelected"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeClips(handle: handle) -> None:
            method = "Pixera.Timelines.Layer.removeClips"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setHomeScreenFromScreenName(handle: handle, screenName: str) -> None:
            method = "Pixera.Timelines.Layer.setHomeScreenFromScreenName"
            params = ["handle, screenName"]

            return [method, params, [handle, screenName]]

        @staticmethod
        def getHomeScreenName(handle: handle) -> str:
            method = "Pixera.Timelines.Layer.getHomeScreenName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setBlendMode(handle: handle, blendMode: str) -> None:
            method = "Pixera.Timelines.Layer.setBlendMode"
            params = ["handle, blendMode"]

            return [method, params, [handle, blendMode]]

        @staticmethod
        def getBlendMode(handle: handle) -> str:
            method = "Pixera.Timelines.Layer.getBlendMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def addEffectById(handle: handle, id: float) -> None:
            method = "Pixera.Timelines.Layer.addEffectById"
            params = ["handle, id"]

            return [method, params, [handle, id]]

        @staticmethod
        def setPreloadPermanently(handle: handle, doPreloadPermanently: bool) -> None:
            method = "Pixera.Timelines.Layer.setPreloadPermanently"
            params = ["handle, doPreloadPermanently"]

            return [method, params, [handle, doPreloadPermanently]]

        @staticmethod
        def getPreloadPermanently(handle: handle) -> bool:
            method = "Pixera.Timelines.Layer.getPreloadPermanently"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setRestrictToServiceWithIps(handle: handle, doRestrict: bool, ipAdresses: List[str]) -> None:
            method = "Pixera.Timelines.Layer.setRestrictToServiceWithIps"
            params = ["handle, doRestrict, ipAdresses"]

            return [method, params, [handle, doRestrict, ipAdresses]]

        @staticmethod
        def getRestrictToService(handle: handle) -> bool:
            method = "Pixera.Timelines.Layer.getRestrictToService"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getRestrictedServiceIps(handle: handle) -> List[str]:
            method = "Pixera.Timelines.Layer.getRestrictedServiceIps"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getOffsets(handle: handle) -> List[float]:
            method = "Pixera.Timelines.Layer.getOffsets"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setOffsets(handle: handle, x: Optional[float], y: Optional[float], z: Optional[float], xr: Optional[float], yr: Optional[float], zr: Optional[float], xScale: Optional[float], yScale: Optional[float], zScale: Optional[float]) -> None:
            method = "Pixera.Timelines.Layer.setOffsets"
            params = ["handle, x, y, z, xr, yr, zr, xScale, yScale, zScale"]

            return [method, params, [handle, x, y, z, xr, yr, zr, xScale, yScale, zScale]]

        @staticmethod
        def setCurrentValuesToOffset(handle: handle, typeIndex: int, resetDominant: Optional[bool], removeKeyframesClips: Optional[bool]) -> None:
            method = "Pixera.Timelines.Layer.setCurrentValuesToOffset"
            params = ["handle, typeIndex, resetDominant, removeKeyframesClips"]

            return [method, params, [handle, typeIndex, resetDominant, removeKeyframesClips]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Layer.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Layer.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Timelines.Layer.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class Clip:
        @staticmethod
        def getId(handle: handle) -> float:
            method = "Pixera.Timelines.Clip.getId"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def removeThis(handle: handle) -> None:
            method = "Pixera.Timelines.Clip.removeThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getTimeline(handle: handle) -> handle:
            method = "Pixera.Timelines.Clip.getTimeline"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTime(handle: handle, time: float) -> None:
            method = "Pixera.Timelines.Clip.setTime"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getTime(handle: handle) -> float:
            method = "Pixera.Timelines.Clip.getTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setDuration(handle: handle, duration: float) -> None:
            method = "Pixera.Timelines.Clip.setDuration"
            params = ["handle, duration"]

            return [method, params, [handle, duration]]

        @staticmethod
        def getDuration(handle: handle) -> float:
            method = "Pixera.Timelines.Clip.getDuration"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setLabel(handle: handle, label: str) -> None:
            method = "Pixera.Timelines.Clip.setLabel"
            params = ["handle, label"]

            return [method, params, [handle, label]]

        @staticmethod
        def getLabel(handle: handle) -> str:
            method = "Pixera.Timelines.Clip.getLabel"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getPlayMode(handle: handle) -> int:
            method = "Pixera.Timelines.Clip.getPlayMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setPlayMode(handle: handle, playMode: int) -> None:
            method = "Pixera.Timelines.Clip.setPlayMode"
            params = ["handle, playMode"]

            return [method, params, [handle, playMode]]

        @staticmethod
        def getSpeed(handle: handle) -> float:
            method = "Pixera.Timelines.Clip.getSpeed"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setSpeed(handle: handle, speed: float) -> None:
            method = "Pixera.Timelines.Clip.setSpeed"
            params = ["handle, speed"]

            return [method, params, [handle, speed]]

        @staticmethod
        def getBlendFrames(handle: handle) -> bool:
            method = "Pixera.Timelines.Clip.getBlendFrames"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setBlendFrames(handle: handle, doFrameblending: bool) -> None:
            method = "Pixera.Timelines.Clip.setBlendFrames"
            params = ["handle, doFrameblending"]

            return [method, params, [handle, doFrameblending]]

        @staticmethod
        def getInpoint(handle: handle) -> float:
            method = "Pixera.Timelines.Clip.getInpoint"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setInpoint(handle: handle, inpoint: float) -> None:
            method = "Pixera.Timelines.Clip.setInpoint"
            params = ["handle, inpoint"]

            return [method, params, [handle, inpoint]]

        @staticmethod
        def getOutpoint(handle: handle) -> float:
            method = "Pixera.Timelines.Clip.getOutpoint"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setOutpoint(handle: handle, inpoint: float) -> None:
            method = "Pixera.Timelines.Clip.setOutpoint"
            params = ["handle, inpoint"]

            return [method, params, [handle, inpoint]]

        @staticmethod
        def assignResource(handle: handle, resId: float, setToResourceDuration: Optional[bool]) -> None:
            method = "Pixera.Timelines.Clip.assignResource"
            params = ["handle, resId, setToResourceDuration"]

            return [method, params, [handle, resId, setToResourceDuration]]

        @staticmethod
        def getAssignedResource(handle: handle) -> handle:
            method = "Pixera.Timelines.Clip.getAssignedResource"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setToResourceDuration(handle: handle) -> None:
            method = "Pixera.Timelines.Clip.setToResourceDuration"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def createEvent(handle: handle, namePath: str, time: float, value: float) -> None:
            method = "Pixera.Timelines.Clip.createEvent"
            params = ["handle, namePath, time, value"]

            return [method, params, [handle, namePath, time, value]]

        @staticmethod
        def createEventInPixelSpace(handle: handle, namePath: str, time: float, value: float) -> None:
            method = "Pixera.Timelines.Clip.createEventInPixelSpace"
            params = ["handle, namePath, time, value"]

            return [method, params, [handle, namePath, time, value]]

        @staticmethod
        def removeEvent(handle: handle, namePath: str, time: float) -> None:
            method = "Pixera.Timelines.Clip.removeEvent"
            params = ["handle, namePath, time"]

            return [method, params, [handle, namePath, time]]

        @staticmethod
        def createPauseCueBeforeClip(handle: handle) -> handle:
            method = "Pixera.Timelines.Clip.createPauseCueBeforeClip"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setColorTransformPath(handle: handle, colorTransformPath: str) -> None:
            method = "Pixera.Timelines.Clip.setColorTransformPath"
            params = ["handle, colorTransformPath"]

            return [method, params, [handle, colorTransformPath]]

        @staticmethod
        def getColorTransformPath(handle: handle) -> str:
            method = "Pixera.Timelines.Clip.getColorTransformPath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def clearColorTransformPath(handle: handle) -> None:
            method = "Pixera.Timelines.Clip.clearColorTransformPath"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getKeyframesAsJsonString(handle: handle) -> str:
            method = "Pixera.Timelines.Clip.getKeyframesAsJsonString"
            params = ["handle"]

            return [method, params, [handle]]

    class Node:
        @staticmethod
        def getParameters(handle: handle) -> List[handle]:
            method = "Pixera.Timelines.Node.getParameters"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Timelines.Node.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getParamWithName(handle: handle, name: str) -> handle:
            method = "Pixera.Timelines.Node.getParamWithName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def setValues(handle: handle, values: List[float]) -> None:
            method = "Pixera.Timelines.Node.setValues"
            params = ["handle, values"]

            return [method, params, [handle, values]]

        @staticmethod
        def getValues(handle: handle) -> List[float]:
            method = "Pixera.Timelines.Node.getValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetValues(handle: handle) -> None:
            method = "Pixera.Timelines.Node.resetValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def storeValues(handle: handle) -> None:
            method = "Pixera.Timelines.Node.storeValues"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def mute(handle: handle) -> None:
            method = "Pixera.Timelines.Node.mute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def unMute(handle: handle) -> None:
            method = "Pixera.Timelines.Node.unMute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def toggleMute(handle: handle) -> None:
            method = "Pixera.Timelines.Node.toggleMute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsMuted(handle: handle) -> bool:
            method = "Pixera.Timelines.Node.getIsMuted"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getTimeline(handle: handle) -> handle:
            method = "Pixera.Timelines.Node.getTimeline"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Node.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Node.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Timelines.Node.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class Param:
        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Timelines.Param.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsChannel(handle: handle) -> bool:
            method = "Pixera.Timelines.Param.getIsChannel"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setValue(handle: handle, value: timelineParamValue) -> None:
            method = "Pixera.Timelines.Param.setValue"
            params = ["handle, value"]

            return [method, params, [handle, value]]

        @staticmethod
        def setValueRelativ(handle: handle, value: float) -> None:
            method = "Pixera.Timelines.Param.setValueRelativ"
            params = ["handle, value"]

            return [method, params, [handle, value]]

        @staticmethod
        def getValue(handle: handle) -> timelineParamValue:
            method = "Pixera.Timelines.Param.getValue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def resetValue(handle: handle) -> None:
            method = "Pixera.Timelines.Param.resetValue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def storeValue(handle: handle) -> None:
            method = "Pixera.Timelines.Param.storeValue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTransportAttributes(handle: handle, mode: int, speed: float, loop: bool, inpoint: int, outpoint: int) -> None:
            method = "Pixera.Timelines.Param.setTransportAttributes"
            params = ["handle, mode, speed, loop, inpoint, outpoint"]

            return [method, params, [handle, mode, speed, loop, inpoint, outpoint]]

        @staticmethod
        def getAttributes(handle: handle) -> TransportAttributes:
            method = "Pixera.Timelines.Param.getAttributes"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def mute(handle: handle) -> None:
            method = "Pixera.Timelines.Param.mute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def unMute(handle: handle) -> None:
            method = "Pixera.Timelines.Param.unMute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def toggleMute(handle: handle) -> None:
            method = "Pixera.Timelines.Param.toggleMute"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIsMuted(handle: handle) -> bool:
            method = "Pixera.Timelines.Param.getIsMuted"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Param.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Param.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Timelines.Param.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    class Cue:
        @staticmethod
        def removeThis(handle: handle) -> None:
            method = "Pixera.Timelines.Cue.removeThis"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def apply(handle: handle, blendDuration: Optional[float]) -> None:
            method = "Pixera.Timelines.Cue.apply"
            params = ["handle, blendDuration"]

            return [method, params, [handle, blendDuration]]

        @staticmethod
        def blendToThis(handle: handle, blendDuration: float) -> None:
            method = "Pixera.Timelines.Cue.blendToThis"
            params = ["handle, blendDuration"]

            return [method, params, [handle, blendDuration]]

        @staticmethod
        def getAttributes(handle: handle) -> CueAttributes:
            method = "Pixera.Timelines.Cue.getAttributes"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getTimeline(handle: handle) -> handle:
            method = "Pixera.Timelines.Cue.getTimeline"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getIndex(handle: handle) -> int:
            method = "Pixera.Timelines.Cue.getIndex"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getName(handle: handle) -> str:
            method = "Pixera.Timelines.Cue.getName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setName(handle: handle, name: str) -> bool:
            method = "Pixera.Timelines.Cue.setName"
            params = ["handle, name"]

            return [method, params, [handle, name]]

        @staticmethod
        def getNote(handle: handle) -> str:
            method = "Pixera.Timelines.Cue.getNote"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setNote(handle: handle, note: str) -> bool:
            method = "Pixera.Timelines.Cue.setNote"
            params = ["handle, note"]

            return [method, params, [handle, note]]

        @staticmethod
        def getOperation(handle: handle) -> int:
            method = "Pixera.Timelines.Cue.getOperation"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setOperation(handle: handle, operation: int) -> bool:
            method = "Pixera.Timelines.Cue.setOperation"
            params = ["handle, operation"]

            return [method, params, [handle, operation]]

        @staticmethod
        def getJumpMode(handle: handle) -> int:
            method = "Pixera.Timelines.Cue.getJumpMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setJumpMode(handle: handle, jumpMode: int) -> bool:
            method = "Pixera.Timelines.Cue.setJumpMode"
            params = ["handle, jumpMode"]

            return [method, params, [handle, jumpMode]]

        @staticmethod
        def getJumpGoalTime(handle: handle) -> float:
            method = "Pixera.Timelines.Cue.getJumpGoalTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setJumpGoalTime(handle: handle, time: float) -> bool:
            method = "Pixera.Timelines.Cue.setJumpGoalTime"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getJumpGoalLabel(handle: handle) -> str:
            method = "Pixera.Timelines.Cue.getJumpGoalLabel"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getJumpGoalCue(handle: handle) -> handle:
            method = "Pixera.Timelines.Cue.getJumpGoalCue"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setJumpGoalLabel(handle: handle, jumpGoalLabel: str) -> bool:
            method = "Pixera.Timelines.Cue.setJumpGoalLabel"
            params = ["handle, jumpGoalLabel"]

            return [method, params, [handle, jumpGoalLabel]]

        @staticmethod
        def getNumber(handle: handle) -> int:
            method = "Pixera.Timelines.Cue.getNumber"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setNumber(handle: handle, number: int) -> None:
            method = "Pixera.Timelines.Cue.setNumber"
            params = ["handle, number"]

            return [method, params, [handle, number]]

        @staticmethod
        def getWaitDuration(handle: handle) -> float:
            method = "Pixera.Timelines.Cue.getWaitDuration"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setWaitDuration(handle: handle, time: float) -> bool:
            method = "Pixera.Timelines.Cue.setWaitDuration"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getBlendDuration(handle: handle) -> float:
            method = "Pixera.Timelines.Cue.getBlendDuration"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setBlendDuration(handle: handle, timeInFrames: float) -> bool:
            method = "Pixera.Timelines.Cue.setBlendDuration"
            params = ["handle, timeInFrames"]

            return [method, params, [handle, timeInFrames]]

        @staticmethod
        def getTime(handle: handle) -> float:
            method = "Pixera.Timelines.Cue.getTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTime(handle: handle, time: float) -> bool:
            method = "Pixera.Timelines.Cue.setTime"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def getTimelineToTriggerName(handle: handle) -> str:
            method = "Pixera.Timelines.Cue.getTimelineToTriggerName"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTimelineToTrigger(handle: handle, nameTimeline: str) -> bool:
            method = "Pixera.Timelines.Cue.setTimelineToTrigger"
            params = ["handle, nameTimeline"]

            return [method, params, [handle, nameTimeline]]

        @staticmethod
        def getTimelineTriggerMode(handle: handle) -> int:
            method = "Pixera.Timelines.Cue.getTimelineTriggerMode"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTimelineTriggerMode(handle: handle, mode: int) -> bool:
            method = "Pixera.Timelines.Cue.setTimelineTriggerMode"
            params = ["handle, mode"]

            return [method, params, [handle, mode]]

        @staticmethod
        def getTimelineTriggerApplyTime(handle: handle) -> float:
            method = "Pixera.Timelines.Cue.getTimelineTriggerApplyTime"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setTimelineTriggerApplyTime(handle: handle, time: float) -> bool:
            method = "Pixera.Timelines.Cue.setTimelineTriggerApplyTime"
            params = ["handle, time"]

            return [method, params, [handle, time]]

        @staticmethod
        def setTimelineTriggerApplyCue(handle: handle, goalCueLabel: str) -> bool:
            method = "Pixera.Timelines.Cue.setTimelineTriggerApplyCue"
            params = ["handle, goalCueLabel"]

            return [method, params, [handle, goalCueLabel]]

        @staticmethod
        def getCountdown(handle: handle) -> float:
            method = "Pixera.Timelines.Cue.getCountdown"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def getCountdownHMSF(handle: handle) -> str:
            method = "Pixera.Timelines.Cue.getCountdownHMSF"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def setCommand(handle: handle, conveyorName: str, commandData: str) -> None:
            method = "Pixera.Timelines.Cue.setCommand"
            params = ["handle, conveyorName, commandData"]

            return [method, params, [handle, conveyorName, commandData]]

        @staticmethod
        def getInst(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Cue.getInst"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getHandleFromInstancePath(handle: handle, instancePath: str) -> handle:
            method = "Pixera.Timelines.Cue.getHandleFromInstancePath"
            params = ["handle, instancePath"]

            return [method, params, [handle, instancePath]]

        @staticmethod
        def getInstancePath(handle: handle) -> str:
            method = "Pixera.Timelines.Cue.getInstancePath"
            params = ["handle"]

            return [method, params, [handle]]

    @staticmethod
    def setMarkerPositions(positions: List[float], markerIds: List[int]) -> None:
        method = "Pixera.Calibration.setMarkerPositions"
        params = ["positions", "markerIds"]
        return [method, params, [positions, markerIds]]

    @staticmethod
    def loadDeviceUi(devicePath: str) -> None:
        method = "Pixera.WebViews.loadDeviceUi"
        params = ["devicePath"]
        return [method, params, [devicePath]]

    @staticmethod
    def activatePreviousFunc() -> None:
        method = "Pixera.WebViews.activatePreviousFunc"
        params = []
        return [method, params, []]

    @staticmethod
    def activateNextFunc() -> None:
        method = "Pixera.WebViews.activateNextFunc"
        params = []
        return [method, params, []]

    @staticmethod
    def getLastActivatedFunc() -> str:
        method = "Pixera.WebViews.getLastActivatedFunc"
        params = []
        return [method, params, []]

    @staticmethod
    def deviceActivated(devicePath: str, withSelection: bool) -> None:
        method = "Pixera.WebViews.deviceActivated"
        params = ["devicePath", "withSelection"]
        return [method, params, [devicePath, withSelection]]

    @staticmethod
    def funcActivated(funcPath: str, withSelection: bool) -> None:
        method = "Pixera.WebViews.funcActivated"
        params = ["funcPath", "withSelection"]
        return [method, params, [funcPath, withSelection]]

    @staticmethod
    def setFuncBodyState(funcPath: str, state: str) -> None:
        method = "Pixera.WebViews.setFuncBodyState"
        params = ["funcPath", "state"]
        return [method, params, [funcPath, state]]

    @staticmethod
    def getFuncBodyState(funcPath: str) -> str:
        method = "Pixera.WebViews.getFuncBodyState"
        params = ["funcPath"]
        return [method, params, [funcPath]]

    @staticmethod
    def setTag(tag: str, text: str) -> None:
        method = "Pixera.WebViews.setTag"
        params = ["tag", "text"]
        return [method, params, [tag, text]]

    @staticmethod
    def setEditorIsUsingBlocks(useBlocks: bool) -> None:
        method = "Pixera.WebViews.setEditorIsUsingBlocks"
        params = ["useBlocks"]
        return [method, params, [useBlocks]]

    @staticmethod
    def getComboBoxWithId(id: float) -> handle:
        method = "Pixera.Ui.getComboBoxWithId"
        params = ["id"]
        return [method, params, [id]]

    @staticmethod
    def setAppMode(mode: int) -> None:
        method = "Pixera.Ui.setAppMode"
        params = ["mode"]
        return [method, params, [mode]]

    @staticmethod
    def getAppMode() -> int:
        method = "Pixera.Ui.getAppMode"
        params = []
        return [method, params, []]

    @staticmethod
    def getDisplayTestpattern() -> bool:
        method = "Pixera.Ui.getDisplayTestpattern"
        params = []
        return [method, params, []]

    @staticmethod
    def setDisplayTestpattern(display: bool) -> None:
        method = "Pixera.Ui.setDisplayTestpattern"
        params = ["display"]
        return [method, params, [display]]

    @staticmethod
    def getPreviewCameraAsJsonString() -> str:
        method = "Pixera.Ui.getPreviewCameraAsJsonString"
        params = []
        return [method, params, []]

    @staticmethod
    def setPreviewCameraAsJsonString(cameraFrustrumStateString: str) -> None:
        method = "Pixera.Ui.setPreviewCameraAsJsonString"
        params = ["cameraFrustrumStateString"]
        return [method, params, [cameraFrustrumStateString]]

    @staticmethod
    def setDisableContentRendering(state: bool) -> None:
        method = "Pixera.Ui.setDisableContentRendering"
        params = ["state"]
        return [method, params, [state]]

    @staticmethod
    def getIsContentRenderingDisabled() -> bool:
        method = "Pixera.Ui.getIsContentRenderingDisabled"
        params = []
        return [method, params, []]

    @staticmethod
    def setDisableWorkspaceRendering(state: bool) -> None:
        method = "Pixera.Ui.setDisableWorkspaceRendering"
        params = ["state"]
        return [method, params, [state]]

    @staticmethod
    def getIsWorkspaceRenderingDisabled() -> bool:
        method = "Pixera.Ui.getIsWorkspaceRenderingDisabled"
        params = []
        return [method, params, []]

    class ComboBox:
        @staticmethod
        def clear(handle: handle) -> None:
            method = "Pixera.Ui.ComboBox.clear"
            params = ["handle"]

            return [method, params, [handle]]

        @staticmethod
        def addItem(handle: handle, item: str, id: int) -> None:
            method = "Pixera.Ui.ComboBox.addItem"
            params = ["handle, item, id"]

            return [method, params, [handle, item, id]]

        @staticmethod
        def setSelectedId(handle: handle, id: int) -> None:
            method = "Pixera.Ui.ComboBox.setSelectedId"
            params = ["handle, id"]

            return [method, params, [handle, id]]

        @staticmethod
        def getSelectedId(handle: handle) -> int:
            method = "Pixera.Ui.ComboBox.getSelectedId"
            params = ["handle"]

            return [method, params, [handle]]

    @staticmethod
    def setRegistered(hdls: List[handle], expectedFrequency: int, dampingMs: int, usageHints: List[str]) -> None:
        method = "Pixera.Direct.setRegistered"
        params = ["hdls", "expectedFrequency", "dampingMs", "usageHints"]
        return [method, params, [hdls, expectedFrequency, dampingMs, usageHints]]

    @staticmethod
    def reloadRegistered() -> None:
        method = "Pixera.Direct.reloadRegistered"
        params = []
        return [method, params, []]

    @staticmethod
    def registerScreen(name: str, expectedFrequency: int, dampingMs: int) -> handle:
        method = "Pixera.Direct.registerScreen"
        params = ["name", "expectedFrequency", "dampingMs"]
        return [method, params, [name, expectedFrequency, dampingMs]]

    @staticmethod
    def registerParam(instancePath: str) -> handle:
        method = "Pixera.Direct.registerParam"
        params = ["instancePath"]
        return [method, params, [instancePath]]

    @staticmethod
    def registerCamera(cameraName: str, expectedFrequency: int) -> handle:
        method = "Pixera.Direct.registerCamera"
        params = ["cameraName", "expectedFrequency"]
        return [method, params, [cameraName, expectedFrequency]]

    @staticmethod
    def registerPerspective(screenName: str, expectedFrequency: int) -> handle:
        method = "Pixera.Direct.registerPerspective"
        params = ["screenName", "expectedFrequency"]
        return [method, params, [screenName, expectedFrequency]]

    class Camera:
        @staticmethod
        def setPosition(handle: handle, xPos: float, yPos: float, zPos: float) -> None:
            method = "Pixera.Direct.Camera.setPosition"
            params = ["handle, xPos, yPos, zPos"]

            return [method, params, [handle, xPos, yPos, zPos]]

        @staticmethod
        def setRotation(handle: handle, xRot: float, yRot: float, zRot: float) -> None:
            method = "Pixera.Direct.Camera.setRotation"
            params = ["handle, xRot, yRot, zRot"]

            return [method, params, [handle, xRot, yRot, zRot]]

        @staticmethod
        def setTransformation(handle: handle, xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float) -> None:
            method = "Pixera.Direct.Camera.setTransformation"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio]]

        @staticmethod
        def setTransformationAndLensProps(handle: handle, xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, iris: float, k1: float, k2: float, centerX: float, centerY: float, panelWidth: float) -> None:
            method = "Pixera.Direct.Camera.setTransformationAndLensProps"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, iris, k1, k2, centerX, centerY, panelWidth]]

        @staticmethod
        def setTransformationAndLensPropsExt(handle: handle, xPos: float, yPos: float, zPos: float, xRot: float, yRot: float, zRot: float, fov: float, aspectRatio: float, nearClip: float, farClip: float, aperture: float, focus: float, focalDistance: float, zoom: float, iris: float, k1: float, k2: float, k3: float, p1: float, p2: float, centerX: float, centerY: float, panelWidth: float, overscan: float) -> None:
            method = "Pixera.Direct.Camera.setTransformationAndLensPropsExt"
            params = ["handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, focalDistance, zoom, iris, k1, k2, k3, p1, p2, centerX, centerY, panelWidth, overscan"]

            return [method, params, [handle, xPos, yPos, zPos, xRot, yRot, zRot, fov, aspectRatio, nearClip, farClip, aperture, focus, focalDistance, zoom, iris, k1, k2, k3, p1, p2, centerX, centerY, panelWidth, overscan]]

    @staticmethod
    def getSupportedUnrealPluginVersion() -> int:
        method = "Pixera.Unreal.Utility.getSupportedUnrealPluginVersion"
        params = []
        return [method, params, []]

