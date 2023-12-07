import shutil
#s hutil.copy('dummyFolder/copyMe.ruby', 'automateTheBoringStuff') # copy file and paste it in the given directory
# shutil.copy('dummyFolder/copyMe.ruby', 'automateTheBoringStuff/renamed.ruby') 

# shutil.copytree('dummyFolder', 'dummyFolderBackup') # copy folder and paste it in the given directory

shutil.move('automateTheBoringStuff/renamed.ruby', 'dummyFolder') # move file to the given directory