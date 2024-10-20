from idlelib.configHandler import idleConf
menudefs = [
 (
  'file',
  [
   ('_New File', '<<open-new-window>>'),
   ('_Open...', '<<open-window-from-file>>'),
   ('Open _Module...', '<<open-module>>'),
   ('Class _Browser', '<<open-class-browser>>'),
   ('_Path Browser', '<<open-path-browser>>'),
   None,
   ('_Save', '<<save-window>>'),
   ('Save _As...', '<<save-window-as-file>>'),
   ('Save Cop_y As...', '<<save-copy-of-window-as-file>>'),
   None,
   ('Prin_t Window', '<<print-window>>'),
   None,
   ('_Close', '<<close-window>>'),
   ('E_xit', '<<close-all-windows>>')]),
 (
  'edit',
  [
   ('_Undo', '<<undo>>'),
   ('_Redo', '<<redo>>'),
   None,
   ('Cu_t', '<<cut>>'),
   ('_Copy', '<<copy>>'),
   ('_Paste', '<<paste>>'),
   ('Select _All', '<<select-all>>'),
   None,
   ('_Find...', '<<find>>'),
   ('Find A_gain', '<<find-again>>'),
   ('Find _Selection', '<<find-selection>>'),
   ('Find in Files...', '<<find-in-files>>'),
   ('R_eplace...', '<<replace>>'),
   ('Go to _Line', '<<goto-line>>')]),
 (
  'format',
  [
   ('_Indent Region', '<<indent-region>>'),
   ('_Dedent Region', '<<dedent-region>>'),
   ('Comment _Out Region', '<<comment-region>>'),
   ('U_ncomment Region', '<<uncomment-region>>'),
   ('Tabify Region', '<<tabify-region>>'),
   ('Untabify Region', '<<untabify-region>>'),
   ('Toggle Tabs', '<<toggle-tabs>>'),
   ('New Indent Width', '<<change-indentwidth>>')]),
 (
  'run',
  [
   ('Python Shell', '<<open-python-shell>>')]),
 (
  'shell',
  [
   ('_View Last Restart', '<<view-restart>>'),
   ('_Restart Shell', '<<restart-shell>>'),
   None,
   ('_Interrupt Execution', '<<interrupt-execution>>')]),
 (
  'debug',
  [
   ('_Go to File/Line', '<<goto-file-line>>'),
   ('!_Debugger', '<<toggle-debugger>>'),
   ('_Stack Viewer', '<<open-stack-viewer>>'),
   ('!_Auto-open Stack Viewer', '<<toggle-jit-stack-viewer>>')]),
 (
  'options',
  [
   ('Configure _IDLE', '<<open-config-dialog>>'),
   None]),
 (
  'help',
  [
   ('_About IDLE', '<<about-idle>>'),
   None,
   ('_IDLE Help', '<<help>>'),
   ('Python _Docs', '<<python-docs>>')])]
default_keydefs = idleConf.GetCurrentKeySet()