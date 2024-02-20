var batteries = ["battery1", "battery2", "battery3", "battery4"];

// Helper function to check if at least one element in an array satisfies a condition
var hasEmptyBattery = function (battery_states) {
    return reduce(function(acc, state) { return acc || (state === "empty"); }, false, battery_states);
};

// Question a: Opened 4-pack, at least 3 or more batteries are full
var gen_a_more = function () {
    var battery_states = map(function () { return flip(0.1) ? "empty" : "full"; }, batteries);
    return hasEmptyBattery(battery_states) && filter(function(state) { return state === "full"; }, battery_states).length >= 3;
}

// Question a: Opened 4-pack, only 3 batteries are full
var gen_a = function () {
    var battery_states = map(function () { return flip(0.1) ? "empty" : "full"; }, batteries);
    return hasEmptyBattery(battery_states) && filter(function(state) { return state === "full"; }, battery_states).length === 3;
}

// Question b: Opened a new pack, first battery is half-empty
var gen_b = function () {
    var battery_states = ["empty"].concat(map(function () { return flip(0.1) ? "empty" : "full"; }, batteries.slice(1)));
    //print(battery_states)
    return filter(function(state) { return state === "full"; }, battery_states.slice(1)).length === 3;
}

print("Opened 4-pack, at least 3 or more batteries are full")
var a = Infer({ method: 'rejection', samples: 10000 }, gen_a_more)
print(a)
viz(a);

print("Opened 4-pack, only 3 batteries are full")
var a = Infer({ method: 'rejection', samples: 10000 }, gen_a)
print(a)
viz(a);

print("Opened a new pack, first battery is half-empty")
var b = Infer({ method: 'rejection', samples: 10000 }, gen_b)
print(b)
viz(b);
