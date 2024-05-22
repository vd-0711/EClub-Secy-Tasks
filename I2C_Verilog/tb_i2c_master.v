`timescale 1ns / 1ns

module tb_i2c_master;
    reg clk;
    reg start;
    wire scl;
    wire sda;
    
    // Instantiate the I2C_Simple module
    I2C_Simple uut (
        .clk(clk),
        .start(start),
        .scl(scl),
        .sda(sda)
    );

    // Generate clock signal
    always #5 clk = ~clk; // 100 MHz clock (10ns period)

    initial begin
        // Initialize inputs
        clk = 0;
        start = 0;

        // Apply stimulus
        #20 start = 1; // Assert start after 20ns
        #10 start = 0; // De-assert start after 10ns

        // Wait for some time to observe the outputs
        #100 $finish;
    end

    // Dump waveform data for GTKWave
    initial begin
        $dumpfile("tb_i2c_master.vcd");
        $dumpvars(0, tb_i2c_master);
    end
endmodule
