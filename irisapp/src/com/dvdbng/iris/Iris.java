package com.dvdbng.iris;

import java.util.Calendar;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.widget.Toast;

public class Iris extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }
    Toast mToast;
    public void test(View view){
        ((Button)view).setText("test");
        //Intent alarmIntent = new Intent(Iris.this,AlarmReceiver.class);

        //PendingIntent sender = PendingIntent.getBroadcast(Iris.this, 0, alarmIntent, PendingIntent.FLAG_UPDATE_CURRENT);

        //Calendar cal = Calendar.getInstance();
        //cal.setTimeInMillis(System.currentTimeMillis());
        //cal.add(Calendar.SECOND, 2);

        //AlarmManager am = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
        //am.set(AlarmManager.RTC_WAKEUP, cal.getTimeInMillis(), sender);
        //((Button)view).setText("testa4");
        //Toast.makeText(this, new Long(cal.getTimeInMillis()).toString(), Toast.LENGTH_SHORT).show();

            Intent intent = new Intent(Iris.this, AlarmReceiver.class);
            PendingIntent sender = PendingIntent.getBroadcast(Iris.this,
                    0, intent, 0);

            // We want the alarm to go off 30 seconds from now.
            Calendar calendar = Calendar.getInstance();
            calendar.setTimeInMillis(System.currentTimeMillis());
            calendar.add(Calendar.SECOND, 10);

            // Schedule the alarm!
            AlarmManager am = (AlarmManager)getSystemService(ALARM_SERVICE);
            am.set(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), sender);

            // Tell the user about what we did.
            if (mToast != null) {
                mToast.cancel();
            }
            mToast = Toast.makeText(Iris.this, "SCHEDULED",
                    Toast.LENGTH_LONG);
            mToast.show();

    }
}
