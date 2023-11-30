# Copyright 2023 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def cgesdd_rwork_size(m: int, n: int, compute_uv: int) -> int: ...
def cgesdd_work_size(m: int, n: int, job_opt_compute_uv: bool, job_opt_full_matrices: bool) -> int: ...
def dgesdd_work_size(m: int, n: int, job_opt_compute_uv: bool, job_opt_full_matrices: bool) -> int: ...
def gesdd_iwork_size(m: int, n: int) -> int: ...
def heevd_rwork_size(n: int) -> int: ...
def heevd_work_size(n: int) -> int: ...
def initialize() -> None: ...
def lapack_cgehrd_workspace(lda: int, n: int, ilo: int, ihi: int) -> int: ...
def lapack_cgeqrf_workspace(m: int, n: int) -> int: ...
def lapack_chetrd_workspace(lda: int, n: int) -> int: ...
def lapack_cungqr_workspace(m: int, n: int, k: int) -> int: ...
def lapack_dgehrd_workspace(lda: int, n: int, ilo: int, ihi: int) -> int: ...
def lapack_dgeqrf_workspace(m: int, n: int) -> int: ...
def lapack_dorgqr_workspace(m: int, n: int, k: int) -> int: ...
def lapack_dsytrd_workspace(lda: int, n: int) -> int: ...
def lapack_sgehrd_workspace(lda: int, n: int, ilo: int, ihi: int) -> int: ...
def lapack_sgeqrf_workspace(m: int, n: int) -> int: ...
def lapack_sorgqr_workspace(m: int, n: int, k: int) -> int: ...
def lapack_ssytrd_workspace(lda: int, n: int) -> int: ...
def lapack_zgehrd_workspace(lda: int, n: int, ilo: int, ihi: int) -> int: ...
def lapack_zgeqrf_workspace(m: int, n: int) -> int: ...
def lapack_zhetrd_workspace(lda: int, n: int) -> int: ...
def lapack_zungqr_workspace(m: int, n: int, k: int) -> int: ...
def registrations() -> dict: ...
def sgesdd_work_size(m: int, n: int, job_opt_compute_uv: bool, job_opt_full_matrices: bool) -> int: ...
def syevd_iwork_size(n: int) -> int: ...
def syevd_work_size(n: int) -> int: ...
def zgesdd_work_size(m: int, n: int, job_opt_compute_uv: bool, job_opt_full_matrices: bool) -> int: ...
