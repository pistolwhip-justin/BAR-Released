#!/usr/bin/env python3
"""Apply the focused BAR notification Stop-action patch to the pinned upstream source."""
from pathlib import Path

ROOT = Path("upstream/BAR")


def replace_once(path: str, old: str, new: str) -> None:
    file_path = ROOT / path
    source = file_path.read_text(encoding="utf-8")
    count = source.count(old)
    if count != 1:
        raise SystemExit(
            f"Patch safety check failed for {path}: expected one match, found {count}"
        )
    file_path.write_text(source.replace(old, new, 1), encoding="utf-8")


replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/RecorderService.kt",
    '        private val ACTION_RESUME = "${RecorderService::class.java.canonicalName}.RESUME"\n',
    '        private val ACTION_RESUME = "${RecorderService::class.java.canonicalName}.RESUME"\n'
    '        private val ACTION_STOP = "${RecorderService::class.java.canonicalName}.STOP"\n',
)
replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/RecorderService.kt",
    '            ACTION_PAUSE, ACTION_RESUME -> {\n'
    '                recorder?.isPaused = intent.action == ACTION_PAUSE\n'
    '                updateForegroundState()\n'
    '            }\n',
    '            ACTION_PAUSE, ACTION_RESUME -> {\n'
    '                recorder?.isPaused = intent.action == ACTION_PAUSE\n'
    '                updateForegroundState()\n'
    '            }\n'
    '            ACTION_STOP -> requestStopRecording()\n',
)
replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/RecorderService.kt",
    '    private fun createResumeIntent(): PendingIntent =\n'
    '        PendingIntent.getService(\n'
    '            this,\n'
    '            2,\n'
    '            Intent(this, RecorderService::class.java).setAction(ACTION_RESUME),\n'
    '            PendingIntent.FLAG_IMMUTABLE\n'
    '        )\n',
    '    private fun createResumeIntent(): PendingIntent =\n'
    '        PendingIntent.getService(\n'
    '            this,\n'
    '            2,\n'
    '            Intent(this, RecorderService::class.java).setAction(ACTION_RESUME),\n'
    '            PendingIntent.FLAG_IMMUTABLE\n'
    '        )\n'
    '\n'
    '    private fun createStopIntent(): PendingIntent =\n'
    '        PendingIntent.getService(\n'
    '            this,\n'
    '            3,\n'
    '            Intent(this, RecorderService::class.java).setAction(ACTION_STOP),\n'
    '            PendingIntent.FLAG_IMMUTABLE\n'
    '        )\n',
)
replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/RecorderService.kt",
    '                        createResumeIntent()\n'
    '                    )',
    '                        createResumeIntent(),\n'
    '                        R.string.notification_action_stop,\n'
    '                        createStopIntent()\n'
    '                    )',
)
replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/RecorderService.kt",
    '                        createPauseIntent()\n'
    '                    )',
    '                        createPauseIntent(),\n'
    '                        R.string.notification_action_stop,\n'
    '                        createStopIntent()\n'
    '                    )',
)
replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/Notifications.kt",
    '        @StringRes actionText: Int,\n'
    '        actionIntent: PendingIntent,\n'
    '    ): Notification {',
    '        @StringRes actionText: Int,\n'
    '        actionIntent: PendingIntent,\n'
    '        @StringRes stopActionText: Int,\n'
    '        stopActionIntent: PendingIntent,\n'
    '    ): Notification {',
)
replace_once(
    "app/src/main/kotlin/com/patrykmis/bar/Notifications.kt",
    '            addAction(\n'
    '                Notification.Action.Builder(\n'
    '                    null,\n'
    '                    context.getString(actionText),\n'
    '                    actionIntent,\n'
    '                ).build()\n'
    '            )\n',
    '            addAction(\n'
    '                Notification.Action.Builder(\n'
    '                    null,\n'
    '                    context.getString(actionText),\n'
    '                    actionIntent,\n'
    '                ).build()\n'
    '            )\n'
    '            addAction(\n'
    '                Notification.Action.Builder(\n'
    '                    null,\n'
    '                    context.getString(stopActionText),\n'
    '                    stopActionIntent,\n'
    '                ).build()\n'
    '            )\n',
)
replace_once(
    "app/src/main/res/values/strings.xml",
    '    <string name="notification_action_resume">Resume</string>\n',
    '    <string name="notification_action_resume">Resume</string>\n'
    '    <string name="notification_action_stop" translatable="false">Stop</string>\n',
)
print("Applied Stop action patch to RecorderService, Notifications, and strings.xml.")
