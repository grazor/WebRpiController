// Handles toggling switches
function myToggleHandler(e) {
    // How many switches are toggling right now?
    processing++;

    // Data
    var data = { pin : e.srcElement.id.substring(1),
             value: e.detail.isActive 
    };

    console.log("Set pin " + data.pin + " = " + data.value)
    
    // Send request
    $.ajax({
        type: "POST",
        url: "/pin/",
        data: data,
        success: function(data){
            processing--;
        },
        failure: function() {
            processing--;
        }
    });
}

// Set switches' positions according pins' states
function pinStatePolling() {
    // If something is toggling, not to poll states
    if (processing != 0 && !polling) return;
    polling = true;

    // Send request
    $.ajax({
        type: "GET",
        url: "/state/",
        success: function(data){
            pins = JSON.parse(data)
            for (i=0; i < pins.length; i++) {
                if (pins[i].type == 'out') {
                    // Pin state
                    var state = pins[i].state == "on";

                    // Toggling switch
                    var toggle = document.querySelector('.toggle#p'+pins[i].id);
                    var handle      = toggle.querySelector('.toggle-handle');
                    toggle.classList[state ? 'add' : 'remove']('active');

                    var toggleWidth = toggle.clientWidth;
                    var handleWidth = handle.clientWidth;
                    var offset      = toggleWidth - handleWidth;

                    if (state) {
                        handle.style.webkitTransform = 'translate3d(' + offset + 'px,0,0)';
                    } else {
                        handle.style.webkitTransform = 'translate3d(0,0,0)';
                    }
                }
            }

            polling = false;
        },
        failure: function(){
            polling = false;
        }
    });
}



var processing = 0;
var polling = false;


// Polling
if (pollingDelay > 0) {
    var timer = setInterval(pinStatePolling, pollingDelay*1000);
}

// Set toggle handlers
var toggles = document.querySelectorAll('.toggle');
for (i = 0; i < toggles.length; i++) {
    toggles[i].addEventListener('toggle', myToggleHandler, false);
}