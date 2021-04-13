function done=TakeMeas(init,fpath)
    addpath(genpath('.\'))
    done = 1;
    % Initialize Radarstudio .NET connection
    if init==1
        RSTD_DLL_Path = 'C:\ti\mmwave_studio_02_01_01_00\mmWaveStudio\Clients\RtttNetClientController\RtttNetClientAPI.dll';
        ErrStatus = Init_RSTD_Connection(RSTD_DLL_Path);

        if (ErrStatus ~= 30000)
            disp('Error inside Init_RSTD_Connection');
            return;
        end
    else
        %Adjust the save Directory
        Lua_String = "ar1.CaptureCardConfig_StartRecord("+"'"+string(fpath)+"',1)"
        ErrStatus = RtttNetClientAPI.RtttNetClient.SendCommand(Lua_String);
        %Take the Measurement
        Lua_String = "ar1.StartFrame()";
        ErrStatus = RtttNetClientAPI.RtttNetClient.SendCommand(Lua_String);
        
    end
end