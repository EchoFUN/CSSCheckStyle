from helper import *

def doTest():
    _default()

def _default():
    config = parseCkStyleCmdArgs(realpath('ckstyle.ini'), [], [], True)
    equal(config.errorLevel, 0, 'errorLevel is 0')
    equal(config.recursive, False, 'recursive is False')
    equal(config.printFlag, False, 'print flag is False')
    equal(config.include, 'all', 'include is all')
    equal(config.exclude, 'none', 'exclude is none')
    equal(config.extension, '.ckstyle.txt', 'extension is ok')
    equal(config.fixedExtension, '.fixed.css', 'fixed extension is ok')
    equal(len(config.ignoreRuleSets), 1, 'one ruleset to be ignored')

    equal(config.compressConfig.extension, '.min.css', 'extension is .min.css')
    equal(config.compressConfig.combineFile, False, 'combine file is False')
    equal(config.compressConfig.browsers, False, 'browsers is false')

    config = parseCkStyleCmdArgs(realpath('ckstyle.ini'), [("--errorLevel", "2"), ("--include", "abcde"), ("--exclude", "fghi"), ("-p", True), ("-r", True)], [], True)

    equal(config.errorLevel, 2, 'errorLevel is 2')
    equal(config.recursive, True, 'recursive is True')
    equal(config.printFlag, True, 'print flag is True')
    equal(config.include, 'abcde', 'include is abcde')
    equal(config.exclude, 'fghi', 'exclude is fghi')

    config = parseCompressCmdArgs(realpath('ckstyle.ini'), [("--errorLevel", "2"), ("--include", "abcde"), ("--exclude", "fghi"), ("-p", True), ("-r", True), ('--compressExtension', '.xxx.min.css'), ('--browsers', 'true'), ('--combineFile', 'true')], [], True)
    equal(config.errorLevel, 2, 'errorLevel is 2')
    equal(config.recursive, True, 'recursive is True')
    equal(config.printFlag, True, 'print flag is True')
    equal(config.include, 'abcde', 'include is abcde')
    equal(config.exclude, 'fghi', 'exclude is fghi')

    equal(config.compressConfig.extension, '.xxx.min.css', 'extension changed')
    equal(config.compressConfig.combineFile, True, 'combine file is true')
    equal(config.compressConfig.browsers, True, 'browsers is true')

    config = parseFixStyleCmdArgs(realpath('ckstyle.ini'), [("--errorLevel", "2"), ("--include", "abcde"), ("--exclude", "fghi"), ("-p", True), ("-r", True), ('--fixedExtension', '.xxx.fixed.css')], [], True)
    equal(config.errorLevel, 2, 'errorLevel is 2')
    equal(config.recursive, True, 'recursive is True')
    equal(config.printFlag, True, 'print flag is True')
    equal(config.include, 'abcde', 'include is abcde')
    equal(config.exclude, 'fghi', 'exclude is fghi')

    equal(config.fixedExtension, '.xxx.fixed.css', 'fixed extension changed')
