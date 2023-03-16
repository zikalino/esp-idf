# SPDX-FileCopyrightText: 2022-2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

from time import sleep

import pytest
from pytest_embedded import Dut

CONFIGS = [
    pytest.param('default', marks=[pytest.mark.supported_targets, pytest.mark.temp_skip_ci(targets=['esp32h2'], reason='test failed')]),
    pytest.param('freertos_options', marks=[pytest.mark.supported_targets, pytest.mark.temp_skip_ci(targets=['esp32h2'], reason='test failed')]),
    pytest.param('psram', marks=[pytest.mark.esp32]),
    pytest.param('release', marks=[pytest.mark.supported_targets]),
    pytest.param('single_core', marks=[pytest.mark.esp32]),
    pytest.param('smp', marks=[pytest.mark.supported_targets, pytest.mark.temp_skip_ci(targets=['esp32h2'], reason='test failed')]),
]


@pytest.mark.generic
@pytest.mark.parametrize('config', CONFIGS, indirect=True)
def test_freertos(dut: Dut) -> None:
    dut.run_all_single_board_cases()


@pytest.mark.supported_targets
@pytest.mark.generic
@pytest.mark.parametrize('config', ['freertos_options'], indirect=True)
def test_task_notify_too_high_index_fails(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests.')
    dut.write('\"Notify too high index fails\"')
    dut.expect('assert failed: xTaskGenericNotify', timeout=5)
    dut.expect('uxIndexToNotify < [0-9]+')
    dut.expect_exact('Rebooting...')


@pytest.mark.supported_targets
@pytest.mark.generic
@pytest.mark.parametrize('config', ['freertos_options'], indirect=True)
def test_task_notify_wait_too_high_index_fails(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests.')
    dut.write('\"Notify Wait too high index fails\"')
    dut.expect('assert failed: xTaskGenericNotifyWait', timeout=5)
    dut.expect('uxIndexToWait < [0-9]+', timeout=5)
    dut.expect_exact('Rebooting...')


# @pytest.mark.qemu
# @pytest.mark.esp32
# @pytest.mark.parametrize('config', [
#    pytest.param('default', marks=[pytest.mark.supported_targets]),
#    pytest.param('freertos_options', marks=[pytest.mark.supported_targets]),
#    pytest.param('release', marks=[pytest.mark.supported_targets]),
#    pytest.param('single_core', marks=[pytest.mark.esp32]),
#    pytest.param('smp', marks=[pytest.mark.supported_targets]),
#], indirect=True)
#def test_freertos(dut: Dut) -> None:
#    dut.expect_exact('Press ENTER to see the list of tests')
#    sleep(1)
#    dut.write('\n')
#    sleep(1)
#    dut.write('[qemu]')
#    dut.expect_unity_test_output(timeout=300)#


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_event_groups(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS Event Groups"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_event_group_sync(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS Event Group Sync"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_event_group_isr(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS Event Group ISR"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_backported_timer_functions(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS backported timer functions"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_backported_queue_and_semphr_functions(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS backported Queue and Semphr functions"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_static_task_allocation(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS static task allocation"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_backported_eventgroup_functions(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS static task allocation"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_queue_registry(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS Queue Registry"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_queue_sets(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test Queue sets"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_queue_sets_multi_core(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test Queue sets multi-core"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_send_receive_stream_buffer_test(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Send-receive stream buffer test"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_etaskgetstate(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test eTaskGetState"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_scheduling_round_robin(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS Scheduling Round Robin"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_delete_tasks(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS Delete Tasks"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_delete_blocked_tasks(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS Delete Blocked Tasks"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_notify(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test Task_Notify"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_xtaskgethandle(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS xTaskGetHandle()"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_xtaskabortdelay(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FreeRTOS xTaskAbortDelay()"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_trace_utility_functions(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test freertos trace facility functions"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_freertos_ixtaskgetsystemstate(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test freertos uxTaskGetSystemState"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_test_yield_from_lower_priority_task_same_cpu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Yield from lower priority task, same CPU"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_yield_from_lower_priority_task_other_cpu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Yield from lower priority task, other CPU"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_tasks_test_priority_scheduling_smp(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Tasks: Test priority scheduling (SMP)"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_tasks_test_vtaskdelay(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Tasks: Test vTaskDelay"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_tasks_test_vtaskdelayuntil(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Tasks: Test vTaskDelayUntil"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_get_set_priorities(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Get/Set Priorities"')
    dut.expect_unity_test_output(timeout=300)



@pytest.mark.qemu
@pytest.mark.esp32
def test_suspend_resume_task_on_same_core(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Suspend/resume task on same core"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_suspend_the_current_running_task(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Suspend the current running task"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_resume_task_from_isr_same_core(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Resume task from ISR (same core)"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_resume_task_from_isr_other_core(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Resume task from ISR (other core)"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_the_waiting_task_not_missed_both_cpus(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test the waiting task not missed due to scheduler suspension on both CPUs"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_the_waiting_task_not_missed_one_cpu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test the waiting task not missed due to scheduler suspension on one CPU"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_suspend_resume_cpu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test suspend-resume CPU. The number of tick_hook should be the same for both CPUs"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_suspend_resume_cpu_works_with_xtimer(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test suspend-resume CPU works with xTimer"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_vtasksuspend_all_and_xtaskresumeall_basic(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test vTaskSuspendAll and xTaskResumeAll basic"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_vtasksuspend_all_and_xtaskresumeall_multicore(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test vTaskSuspendAll() and xTaskResumeAll() multicore"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_vtasksuspendall_allows_scheduling_on_other_cores(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test vTaskSuspendAll allows scheduling on other cores"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_xtaskresumeall_resumes_pended_tasks(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test xTaskResumeAll resumes pended tasks"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_must_run(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield must run the next ready task of the same priority"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_must_not_run(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield must not run a blocked task"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_must_not_happen_when_scheduler(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield must not happen when scheduler is suspended"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_must_happen_when_a_task_creates(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield must happen when a task creates a higher priority task"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_mist_happen_when_a_task_raises(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield must happed when a task raises the priority of another priority task"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_must_happen_when_issued(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield must happen when issued from another core"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_yield_on_other_core_must_not_happen(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task yield on other core must not happen when scheduler is suspended"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_oneshot_freertos_timers(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Oneshot FreeRTOS timers"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_recurring_freertos_timers(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Recurring FreeRTOS timers"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_static_timer_creation(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Static timer creation"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_for_per_task_non_reentrant_tasks(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test for per-task non-reentrant tasks"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_scheduling_time_test(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"scheduling time test"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_context_save_doesnt_corrupt_return_address_register(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"context save doesn\'t corrupt return address register"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_fpu_usage_in_task(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FPU: Usage in task"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_fpu_usage_in_unpinned_task(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"FPU: Usage in unpinned task"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_xportinisrcontext_test(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"xPortInIsrContext test"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_portmux_spinlocks_no_contention(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"portMUX spinlocks (no contention)"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_portmux_recursive_locks_no_contention(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"portMUX recursive locks (no contention)"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_port_mux_cross_core_locking(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"portMUX cross-core locking"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_port_mux_high_contention(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"portMUX high contention"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_snapshot_get_all(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task snapshot: Get all"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_task_snapshot_iterate(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Task snapshot: Iterate"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_tls_test(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"TLS test"')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_frertos_thread_local_storage_pointers_and_del_cb(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    sleep(1)
    dut.write('"Test FreeRTOS thread local storage pointers and del cb"')
    dut.expect_unity_test_output(timeout=300)
 