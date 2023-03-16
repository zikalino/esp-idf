# SPDX-FileCopyrightText: 2022-2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

from time import sleep

import pytest
from pytest_embedded import Dut


@pytest.mark.esp32
@pytest.mark.esp32s2
@pytest.mark.esp32c3
@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        'default',
        'ringbuf_flash'
    ]
)
def test_esp_ringbuf(dut: Dut) -> None:
    dut.run_all_single_board_cases()


@pytest.mark.esp32
@pytest.mark.qemu
def test_qemu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('![qemu-ignore]')
    dut.expect_unity_test_output(timeout=300)
