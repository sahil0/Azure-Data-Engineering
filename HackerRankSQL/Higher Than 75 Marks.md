![image](https://github.com/sahil0/Azure-Data-Engineering/assets/22682814/729aa345-999c-4ce6-b599-8fc63e16a482)


Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

```
select NAME from STUDENTS WHERE MARKS>75 ORDER BY RIGHT(NAME,3),ID ASC
```
