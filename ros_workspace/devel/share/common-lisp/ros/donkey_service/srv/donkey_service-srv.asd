
(cl:in-package :asdf)

(defsystem "donkey_service-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoInts" :depends-on ("_package_AddTwoInts"))
    (:file "_package_AddTwoInts" :depends-on ("_package"))
    (:file "DegreeData" :depends-on ("_package_DegreeData"))
    (:file "_package_DegreeData" :depends-on ("_package"))
    (:file "DistanceData" :depends-on ("_package_DistanceData"))
    (:file "_package_DistanceData" :depends-on ("_package"))
  ))