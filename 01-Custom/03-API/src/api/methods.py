class Methods:
    def getApiRevision() -> int:
        method = "Pixera.Utility.getApiRevision"
        params = [""]

        return [method,params,[]]

    def getHasFunction(functionName: str) -> bool:
        method = "Pixera.Utility.getHasFunction"
        params = ["functionName"]

    def outputDebug(message: str) -> str:
        method = "Pixera.Utility.outputDebug"
        params = ["message"]

        return [method,params,[message]]

    def getLicenseJson() -> str:
        method = "Pixera.Utility.getLicenseJson"
        params = [""]

    def getCurrentTime() -> float:
        method = "Pixera.Utility.getCurrentTime"
        params = [""]

    def getCurrentTimeAsString() -> str:
        method = "Pixera.Utility.getCurrentTimeAsString"
        params = [""]

    def noop() -> None:
        method = "Pixera.Utility.noop"
        params = [""]

    def requestCallback(functionName: str) -> None:
        method = "Pixera.Utility.requestCallback"
        params = ["functionName"]

    def readFileString(path: str) -> str:
        method = "Pixera.Utility.readFileString"
        params = ["path"]

    def writeFileString(path: str, fileStr: str) -> None:
        method = "Pixera.Utility.writeFileString"
        params = ["path, fileStr"]

    def getAccessRecipe(hdlPath: str) -> str:
        method = "Pixera.Utility.getAccessRecipe"
        params = ["hdlPath"]

    def pollMonitoring() -> str:
        method = "Pixera.Utility.pollMonitoring"
        params = [""]

    def unsubscribeMonitoringSubject(subject: str) -> bool:
        method = "Pixera.Utility.unsubscribeMonitoringSubject"
        params = ["subject"]

    def subscribeMonitoringSubject(subject: str) -> bool:
        method = "Pixera.Utility.subscribeMonitoringSubject"
        params = ["subject"]

    def setMonitoringEventMode(mode: str) -> bool:
        method = "Pixera.Utility.setMonitoringEventMode"
        params = ["mode"]

    def monitoringEvent(eventDescription: str) -> None:
        method = "Pixera.Utility.monitoringEvent"
        params = ["eventDescription"]

    def setShowContextInReplies(doShow: bool) -> bool:
        method = "Pixera.Utility.setShowContextInReplies"
        params = ["doShow"]

    def setMonitoringHasDelimiter(hasDelimiter: bool) -> bool:
        method = "Pixera.Utility.setMonitoringHasDelimiter"
        params = ["hasDelimiter"]

    def runJsScript(jsFunction: str, jsCode: str) -> str:
        method = "Pixera.Utility.runJsScript"
        params = ["jsFunction, jsCode"]