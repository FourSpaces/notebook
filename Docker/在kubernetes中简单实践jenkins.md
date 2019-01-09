



```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
 name: jenkins-pvc
 namespace: development
spec:
 accessModes:
    - ReadWriteOnce
 resources:
   requests:
     storage: 6Gi
```

