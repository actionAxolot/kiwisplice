;; Pony mode configuration file... This is needed to use virtualenv...
;; go figure....
((nil ;; Make sure that it loads regardless of major mode
  (pony-settings . (make-pony-project
                    :python "/Users/axolote/.virtualenvs/kiwi/bin/python"
                    :settings "settings"))))