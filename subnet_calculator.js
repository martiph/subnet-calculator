function cidr_to_subnet_mask(cidr){
    // let raw_int32 = (4294967295).toString(2); // 32 bit string, all 1
    let subnet_bits = Math.pow(2, cidr) - 1;
    subnet_bits = subnet_bits.toString(2).padEnd(32, '0');
    let subnet_mask = '';
    for(let i = 0; i < 32; i += 8){
        if(i != 0){
            subnet_mask += '.'
        }
        subnet_mask += parseInt(subnet_bits.substring(i, i+8), 2);
    }
    return subnet_mask;
}