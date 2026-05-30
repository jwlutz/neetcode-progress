class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = ["root"]
        for l in logs:
            dest = l.replace("/", "")
            match dest:
                case ".":
                    continue
                case "..":
                    if path[-1] == "root":
                        continue
                    path.pop()
                case _:
                    path.append(dest)
        return len(path[1:])
