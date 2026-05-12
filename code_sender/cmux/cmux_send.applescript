on run argv
    tell application "cmux"
        set cmd to (item 1 of argv) as string
        set commit to ((item 2 of argv) as string is "True")
        set t to focused terminal of selected tab of front window
        input text cmd to t
        if commit then
            perform action "text:\r" on t
        end if
    end tell
end run
