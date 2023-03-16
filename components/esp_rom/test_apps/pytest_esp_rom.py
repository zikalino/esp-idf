# SPDX-FileCopyrightText: 2022-2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

from time import sleep

import pytest
from pytest_embedded import Dut


@pytest.mark.esp32c3
@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.esp32c6
@pytest.mark.esp32h2
@pytest.mark.generic
@pytest.mark.nightly_run
def test_esp_rom(dut: Dut) -> None:
    dut.run_all_single_board_cases()


@pytest.mark.qemu
@pytest.mark.esp32
def test_console_qemu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    # dut may not be ready to accept input, so adding the delay until handled in pytest embedded
    sleep(1)
    dut.write('[qemu]')
    dut.expect_unity_test_output(timeout=300)
