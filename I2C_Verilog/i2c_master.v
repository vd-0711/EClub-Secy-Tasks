module I2C_Simple(
    input wire clk,    // Clock input
    input wire start,  // Start signal
    output reg scl,    // Serial Clock Line
    output reg sda     // Serial Data Line
);

reg [1:0] state; // State variable

// State encoding
localparam IDLE = 2'b00,
           SDA_LOW = 2'b01,
           SCL_LOW = 2'b10;

always @(posedge clk) begin
    case (state)
        IDLE: begin
            sda <= 1'b1;
            scl <= 1'b1;
            if (start) begin
                state <= SDA_LOW;
            end
        end
        SDA_LOW: begin
            sda <= 1'b0;
            state <= SCL_LOW;
        end
        SCL_LOW: begin
            scl <= 1'b0;
            state <= IDLE;
        end
        default: begin
            state <= IDLE;
        end
    endcase
end

initial begin
    state = IDLE;
    sda = 1'b1;
    scl = 1'b1;
end

endmodule
