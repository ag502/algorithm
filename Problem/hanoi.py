class Hanoi:
    def move_disk(self, disk_num, start_peg, end_peg):
        print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

    def hanoi(self, num_disks, start_peg, end_peg):
        if num_disks == 1:
            self.move_disk(num_disks, start_peg, end_peg)
            return

        self.hanoi(num_disks - 1, start_peg, 6 - (start_peg + end_peg))
        self.move_disk(num_disks, start_peg, end_peg)
        self.hanoi(num_disks - 1, 6 - (start_peg + end_peg), end_peg)


Hanoi().hanoi(3, 1, 3)
