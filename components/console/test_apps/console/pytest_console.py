# SPDX-FileCopyrightText: 2022-2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

from time import sleep

import pytest
from pytest_embedded import Dut


@pytest.mark.generic
@pytest.mark.supported_targets
def test_console(dut: Dut) -> None:
    dut.run_all_single_board_cases()


@pytest.mark.qemu
@pytest.mark.esp32
def test_console_qemu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    # dut may not be ready to accept input, so adding the delay until handled in pytest embedded
    sleep(1)
    dut.write('[qemu]')
    dut.expect_unity_test_output(timeout=300)
