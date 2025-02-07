# RAN Tester UE Data Processor

To run `parser.py`:

```bash
python3 parser.py {csv_input}

# Example:
# python3 parser.py 2ue_1jammer_uhd_srsgnb.csv
```

To run `plotter.py`:

```bash
python3 plotter.py <input_file> <field_to_plot>

# Example:
# python3 plotter.py output.csv sinr
```
------------------------------------------------------------

List of possible metrics that can be plotted:
* cfo
* distance_km
* dl_earfcn
* dl_evm
* dl_mcs
* fec_iters
* pathloss
* pci
* ri
* rrc_state
* rsrp
* rsrq
* rssi
* rx_brate
* rx_errors
* rx_pkts
* sfo
* sinr
* speed_kmph
* sync_err
* ta_us
* tx_brate
* tx_errors
* tx_pkts
* ul_buffer
* ul_mcs
* ul_power
* dl_tput_mbps
* emm_state
* nof_active_cc
* nof_active_eps_bearer
* proc_rmem
* proc_rmem_kB
* proc_vmem_kB
* rf_l
* rf_o
* rf_u
* sys_mem
* system_load
* ul_dropped_sdus
* ul_tput_mbps

> **_NOTE:_** Example datasets have been provided to tinker with.
