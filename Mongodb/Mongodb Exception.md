**exception in initAndListen: 20 Attempted to create a lock file on a read-only directory: /data/db, terminating**

```
> sudo chmod -R go+w /data/db
or this, which will make the directory owned by you:

> sudo chown -R $USER /data/db
```

