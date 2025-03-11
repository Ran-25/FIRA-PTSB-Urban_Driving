
(cl:in-package :asdf)

(defsystem "acc_urban_service-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "YoloData" :depends-on ("_package_YoloData"))
    (:file "_package_YoloData" :depends-on ("_package"))
  ))