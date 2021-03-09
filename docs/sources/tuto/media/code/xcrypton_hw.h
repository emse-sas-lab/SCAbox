#define XCRYPTON_WORDS_SIZE 4
#define XCRYPTON_BYTES_SIZE 16

#define XCRYPTON_DATA_IN0_OFFSET 0x00
#define XCRYPTON_DATA_IN1_OFFSET 0x04
#define XCRYPTON_DATA_IN2_OFFSET 0x08
#define XCRYPTON_DATA_IN3_OFFSET 0x0C

#define XCRYPTON_DATA_OUT0_OFFSET 0x10
#define XCRYPTON_DATA_OUT1_OFFSET 0x14
#define XCRYPTON_DATA_OUT2_OFFSET 0x18
#define XCRYPTON_DATA_OUT3_OFFSET 0x1C

#define XCRYPTON_DATA_KEY0_OFFSET 0x20
#define XCRYPTON_DATA_KEY1_OFFSET 0x24
#define XCRYPTON_DATA_KEY2_OFFSET 0x28
#define XCRYPTON_DATA_KEY3_OFFSET 0x2c

#define XCRYPTON_STATUS_WR_OFFSET 0x30
#define XCRYPTON_STATUS_RD_OFFSET 0x34

#define XCRYPTON_STATUS_NULL_MASK 0x0
#define XCRYPTON_STATUS_RESET_MASK 0x1
#define XCRYPTON_STATUS_START_MASK 0x2
#define XCRYPTON_STATUS_INV_MASK 0x4
#define XCRYPTON_STATUS_DONE_MASK 0x1

#define XCRYPTON_SetStatus1(status, reg) \
    (reg | status)
#define XCRYPTON_SetStatus0(status, reg) \
    (reg & ~status)
#define XCRYPTON_GetStatus(status, reg) \
    (reg & status)

#define XCRYPTON_ReadReg(addr, offset) \
    Xil_In32((addr) + (offset))
#define XCRYPTON_WriteReg(addr, offset, data) \
    Xil_Out32((addr) + (offset), (data))