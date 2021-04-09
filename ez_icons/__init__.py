import os

class Color:
    black = "black"
    white = "white"

class Icons:
    three_d_rotation = "3d_rotation.png"
    accessibility = "accessibility.png"
    accessible = "accessible.png"
    access_alarm = "access_alarm.png"
    access_alarms = "access_alarms.png"
    access_time = "access_time.png"
    account_balance = "account_balance.png"
    account_balance_wallet = "account_balance_wallet.png"
    account_box = "account_box.png"
    account_circle = "account_circle.png"
    ac_unit = "ac_unit.png"
    adb = "adb.png"
    add = "add.png"
    add_alarm = "add_alarm.png"
    add_alert = "add_alert.png"
    add_a_photo = "add_a_photo.png"
    add_box = "add_box.png"
    add_circle = "add_circle.png"
    add_circle_outline = "add_circle_outline.png"
    add_location = "add_location.png"
    add_shopping_cart = "add_shopping_cart.png"
    add_to_photos = "add_to_photos.png"
    add_to_queue = "add_to_queue.png"
    adjust = "adjust.png"
    airline_seat_flat = "airline_seat_flat.png"
    airline_seat_flat_angled = "airline_seat_flat_angled.png"
    airline_seat_individual_suite = "airline_seat_individual_suite.png"
    airline_seat_legroom_extra = "airline_seat_legroom_extra.png"
    airline_seat_legroom_normal = "airline_seat_legroom_normal.png"
    airline_seat_legroom_reduced = "airline_seat_legroom_reduced.png"
    airline_seat_recline_extra = "airline_seat_recline_extra.png"
    airline_seat_recline_normal = "airline_seat_recline_normal.png"
    airplanemode_active = "airplanemode_active.png"
    airplanemode_inactive = "airplanemode_inactive.png"
    airplay = "airplay.png"
    airport_shuttle = "airport_shuttle.png"
    alarm = "alarm.png"
    alarm_add = "alarm_add.png"
    alarm_off = "alarm_off.png"
    alarm_on = "alarm_on.png"
    album = "album.png"
    all_inclusive = "all_inclusive.png"
    all_out = "all_out.png"
    android = "android.png"
    announcement = "announcement.png"
    apps = "apps.png"
    archive = "archive.png"
    arrow_back = "arrow_back.png"
    arrow_downward = "arrow_downward.png"
    arrow_drop_down = "arrow_drop_down.png"
    arrow_drop_down_circle = "arrow_drop_down_circle.png"
    arrow_drop_up = "arrow_drop_up.png"
    arrow_forward = "arrow_forward.png"
    arrow_upward = "arrow_upward.png"
    art_track = "art_track.png"
    aspect_ratio = "aspect_ratio.png"
    assessment = "assessment.png"
    assignment = "assignment.png"
    assignment_ind = "assignment_ind.png"
    assignment_late = "assignment_late.png"
    assignment_return = "assignment_return.png"
    assignment_returned = "assignment_returned.png"
    assignment_turned_in = "assignment_turned_in.png"
    assistant = "assistant.png"
    assistant_photo = "assistant_photo.png"
    attachment = "attachment.png"
    attach_file = "attach_file.png"
    attach_money = "attach_money.png"
    audiotrack = "audiotrack.png"
    autorenew = "autorenew.png"
    av_timer = "av_timer.png"
    backspace = "backspace.png"
    backup = "backup.png"
    battery_20 = "battery_20.png"
    battery_30 = "battery_30.png"
    battery_50 = "battery_50.png"
    battery_60 = "battery_60.png"
    battery_80 = "battery_80.png"
    battery_90 = "battery_90.png"
    battery_alert = "battery_alert.png"
    battery_charging_20 = "battery_charging_20.png"
    battery_charging_30 = "battery_charging_30.png"
    battery_charging_50 = "battery_charging_50.png"
    battery_charging_60 = "battery_charging_60.png"
    battery_charging_80 = "battery_charging_80.png"
    battery_charging_90 = "battery_charging_90.png"
    battery_charging_full = "battery_charging_full.png"
    battery_full = "battery_full.png"
    battery_std = "battery_std.png"
    battery_unknown = "battery_unknown.png"
    beach_access = "beach_access.png"
    beenhere = "beenhere.png"
    block = "block.png"
    bluetooth = "bluetooth.png"
    bluetooth_audio = "bluetooth_audio.png"
    bluetooth_connected = "bluetooth_connected.png"
    bluetooth_disabled = "bluetooth_disabled.png"
    bluetooth_searching = "bluetooth_searching.png"
    blur_circular = "blur_circular.png"
    blur_linear = "blur_linear.png"
    blur_off = "blur_off.png"
    blur_on = "blur_on.png"
    book = "book.png"
    bookmark = "bookmark.png"
    bookmark_border = "bookmark_border.png"
    border_all = "border_all.png"
    border_bottom = "border_bottom.png"
    border_clear = "border_clear.png"
    border_color = "border_color.png"
    border_horizontal = "border_horizontal.png"
    border_inner = "border_inner.png"
    border_left = "border_left.png"
    border_outer = "border_outer.png"
    border_right = "border_right.png"
    border_style = "border_style.png"
    border_top = "border_top.png"
    border_vertical = "border_vertical.png"
    branding_watermark = "branding_watermark.png"
    brightness_1 = "brightness_1.png"
    brightness_2 = "brightness_2.png"
    brightness_3 = "brightness_3.png"
    brightness_4 = "brightness_4.png"
    brightness_5 = "brightness_5.png"
    brightness_6 = "brightness_6.png"
    brightness_7 = "brightness_7.png"
    brightness_auto = "brightness_auto.png"
    brightness_high = "brightness_high.png"
    brightness_low = "brightness_low.png"
    brightness_medium = "brightness_medium.png"
    broken_image = "broken_image.png"
    brush = "brush.png"
    bubble_chart = "bubble_chart.png"
    bug_report = "bug_report.png"
    build = "build.png"
    burst_mode = "burst_mode.png"
    business = "business.png"
    business_center = "business_center.png"
    cached = "cached.png"
    cake = "cake.png"
    call = "call.png"
    call_end = "call_end.png"
    call_made = "call_made.png"
    call_merge = "call_merge.png"
    call_missed = "call_missed.png"
    call_missed_outgoing = "call_missed_outgoing.png"
    call_received = "call_received.png"
    call_split = "call_split.png"
    call_to_action = "call_to_action.png"
    camera = "camera.png"
    camera_alt = "camera_alt.png"
    camera_enhance = "camera_enhance.png"
    camera_front = "camera_front.png"
    camera_rear = "camera_rear.png"
    camera_roll = "camera_roll.png"
    cancel = "cancel.png"
    card_giftcard = "card_giftcard.png"
    card_membership = "card_membership.png"
    card_travel = "card_travel.png"
    casino = "casino.png"
    cast = "cast.png"
    cast_connected = "cast_connected.png"
    center_focus_strong = "center_focus_strong.png"
    center_focus_weak = "center_focus_weak.png"
    change_history = "change_history.png"
    chat = "chat.png"
    chat_bubble = "chat_bubble.png"
    chat_bubble_outline = "chat_bubble_outline.png"
    check = "check.png"
    check_circle = "check_circle.png"
    chevron_left = "chevron_left.png"
    chevron_right = "chevron_right.png"
    child_care = "child_care.png"
    child_friendly = "child_friendly.png"
    chrome_reader_mode = "chrome_reader_mode.png"
    class_ = "class.png"
    clear = "clear.png"
    clear_all = "clear_all.png"
    close = "close.png"
    closed_caption = "closed_caption.png"
    cloud = "cloud.png"
    cloud_circle = "cloud_circle.png"
    cloud_done = "cloud_done.png"
    cloud_download = "cloud_download.png"
    cloud_off = "cloud_off.png"
    cloud_queue = "cloud_queue.png"
    cloud_upload = "cloud_upload.png"
    code = "code.png"
    collections = "collections.png"
    collections_bookmark = "collections_bookmark.png"
    colorize = "colorize.png"
    color_lens = "color_lens.png"
    comment = "comment.png"
    compare = "compare.png"
    compare_arrows = "compare_arrows.png"
    computer = "computer.png"
    confirmation_number = "confirmation_number.png"
    contacts = "contacts.png"
    contact_mail = "contact_mail.png"
    contact_phone = "contact_phone.png"
    content_copy = "content_copy.png"
    content_cut = "content_cut.png"
    content_paste = "content_paste.png"
    control_point = "control_point.png"
    control_point_duplicate = "control_point_duplicate.png"
    copyright = "copyright.png"
    create = "create.png"
    create_new_folder = "create_new_folder.png"
    credit_card = "credit_card.png"
    crop = "crop.png"
    crop_16_9 = "crop_16_9.png"
    crop_3_2 = "crop_3_2.png"
    crop_5_4 = "crop_5_4.png"
    crop_7_5 = "crop_7_5.png"
    crop_din = "crop_din.png"
    crop_free = "crop_free.png"
    crop_landscape = "crop_landscape.png"
    crop_original = "crop_original.png"
    crop_portrait = "crop_portrait.png"
    crop_rotate = "crop_rotate.png"
    crop_square = "crop_square.png"
    dashboard = "dashboard.png"
    data_usage = "data_usage.png"
    date_range = "date_range.png"
    dehaze = "dehaze.png"
    delete = "delete.png"
    delete_forever = "delete_forever.png"
    delete_sweep = "delete_sweep.png"
    description = "description.png"
    desktop_mac = "desktop_mac.png"
    desktop_windows = "desktop_windows.png"
    details = "details.png"
    developer_board = "developer_board.png"
    developer_mode = "developer_mode.png"
    devices = "devices.png"
    devices_other = "devices_other.png"
    device_hub = "device_hub.png"
    dialer_sip = "dialer_sip.png"
    dialpad = "dialpad.png"
    directions = "directions.png"
    directions_bike = "directions_bike.png"
    directions_boat = "directions_boat.png"
    directions_bus = "directions_bus.png"
    directions_car = "directions_car.png"
    directions_railway = "directions_railway.png"
    directions_run = "directions_run.png"
    directions_subway = "directions_subway.png"
    directions_transit = "directions_transit.png"
    directions_walk = "directions_walk.png"
    disc_full = "disc_full.png"
    dns = "dns.png"
    dock = "dock.png"
    domain = "domain.png"
    done = "done.png"
    done_all = "done_all.png"
    donut_large = "donut_large.png"
    donut_small = "donut_small.png"
    do_not_disturb = "do_not_disturb.png"
    do_not_disturb_alt = "do_not_disturb_alt.png"
    do_not_disturb_off = "do_not_disturb_off.png"
    do_not_disturb_on = "do_not_disturb_on.png"
    drafts = "drafts.png"
    drag_handle = "drag_handle.png"
    drive_eta = "drive_eta.png"
    dvr = "dvr.png"
    edit = "edit.png"
    edit_location = "edit_location.png"
    eject = "eject.png"
    email = "email.png"
    enhanced_encryption = "enhanced_encryption.png"
    equalizer = "equalizer.png"
    error = "error.png"
    error_outline = "error_outline.png"
    euro_symbol = "euro_symbol.png"
    event = "event.png"
    event_available = "event_available.png"
    event_busy = "event_busy.png"
    event_note = "event_note.png"
    event_seat = "event_seat.png"
    ev_station = "ev_station.png"
    exit_to_app = "exit_to_app.png"
    expand_less = "expand_less.png"
    expand_more = "expand_more.png"
    explicit = "explicit.png"
    explore = "explore.png"
    exposure = "exposure.png"
    exposure_neg_1 = "exposure_neg_1.png"
    exposure_neg_2 = "exposure_neg_2.png"
    exposure_plus_1 = "exposure_plus_1.png"
    exposure_plus_2 = "exposure_plus_2.png"
    exposure_zero = "exposure_zero.png"
    extension = "extension.png"
    face = "face.png"
    fast_forward = "fast_forward.png"
    fast_rewind = "fast_rewind.png"
    favorite = "favorite.png"
    favorite_border = "favorite_border.png"
    featured_play_list = "featured_play_list.png"
    featured_video = "featured_video.png"
    feedback = "feedback.png"
    fiber_dvr = "fiber_dvr.png"
    fiber_manual_record = "fiber_manual_record.png"
    fiber_new = "fiber_new.png"
    fiber_pin = "fiber_pin.png"
    fiber_smart_record = "fiber_smart_record.png"
    file_download = "file_download.png"
    file_upload = "file_upload.png"
    filter = "filter.png"
    filter_1 = "filter_1.png"
    filter_2 = "filter_2.png"
    filter_3 = "filter_3.png"
    filter_4 = "filter_4.png"
    filter_5 = "filter_5.png"
    filter_6 = "filter_6.png"
    filter_7 = "filter_7.png"
    filter_8 = "filter_8.png"
    filter_9 = "filter_9.png"
    filter_9_plus = "filter_9_plus.png"
    filter_b_and_w = "filter_b_and_w.png"
    filter_center_focus = "filter_center_focus.png"
    filter_drama = "filter_drama.png"
    filter_frames = "filter_frames.png"
    filter_hdr = "filter_hdr.png"
    filter_list = "filter_list.png"
    filter_none = "filter_none.png"
    filter_tilt_shift = "filter_tilt_shift.png"
    filter_vintage = "filter_vintage.png"
    find_in_page = "find_in_page.png"
    find_replace = "find_replace.png"
    fingerprint = "fingerprint.png"
    first_page = "first_page.png"
    fitness_center = "fitness_center.png"
    flag = "flag.png"
    flare = "flare.png"
    flash_auto = "flash_auto.png"
    flash_off = "flash_off.png"
    flash_on = "flash_on.png"
    flight = "flight.png"
    flight_land = "flight_land.png"
    flight_takeoff = "flight_takeoff.png"
    flip = "flip.png"
    flip_to_back = "flip_to_back.png"
    flip_to_front = "flip_to_front.png"
    folder = "folder.png"
    folder_open = "folder_open.png"
    folder_shared = "folder_shared.png"
    folder_special = "folder_special.png"
    font_download = "font_download.png"
    format_align_center = "format_align_center.png"
    format_align_justify = "format_align_justify.png"
    format_align_left = "format_align_left.png"
    format_align_right = "format_align_right.png"
    format_bold = "format_bold.png"
    format_clear = "format_clear.png"
    format_color_fill = "format_color_fill.png"
    format_color_reset = "format_color_reset.png"
    format_color_text = "format_color_text.png"
    format_indent_decrease = "format_indent_decrease.png"
    format_indent_increase = "format_indent_increase.png"
    format_italblack_48dp = "format_italblack_48dp.png"
    format_line_spacing = "format_line_spacing.png"
    format_list_bulleted = "format_list_bulleted.png"
    format_list_numbered = "format_list_numbered.png"
    format_paint = "format_paint.png"
    format_quote = "format_quote.png"
    format_shapes = "format_shapes.png"
    format_size = "format_size.png"
    format_strikethrough = "format_strikethrough.png"
    format_textdirection_l_to_r = "format_textdirection_l_to_r.png"
    format_textdirection_r_to_l = "format_textdirection_r_to_l.png"
    format_underlined = "format_underlined.png"
    forum = "forum.png"
    forward = "forward.png"
    forward_10 = "forward_10.png"
    forward_30 = "forward_30.png"
    forward_5 = "forward_5.png"
    free_breakfast = "free_breakfast.png"
    fullscreen = "fullscreen.png"
    fullscreen_exit = "fullscreen_exit.png"
    functions = "functions.png"
    gamepad = "gamepad.png"
    games = "games.png"
    gavel = "gavel.png"
    gesture = "gesture.png"
    get_app = "get_app.png"
    gif = "gif.png"
    golf_course = "golf_course.png"
    gps_fixed = "gps_fixed.png"
    gps_not_fixed = "gps_not_fixed.png"
    gps_off = "gps_off.png"
    grade = "grade.png"
    gradient = "gradient.png"
    grain = "grain.png"
    grapheq = "grapheq.png"
    grid_off = "grid_off.png"
    grid_on = "grid_on.png"
    group = "group.png"
    group_add = "group_add.png"
    group_work = "group_work.png"
    g_translate = "g_translate.png"
    hd = "hd.png"
    hdr_off = "hdr_off.png"
    hdr_on = "hdr_on.png"
    hdr_strong = "hdr_strong.png"
    hdr_weak = "hdr_weak.png"
    headset = "headset.png"
    headset_mblack_48dp = "headset_mblack_48dp.png"
    healing = "healing.png"
    hearing = "hearing.png"
    help = "help.png"
    help_outline = "help_outline.png"
    highlight = "highlight.png"
    highlight_off = "highlight_off.png"
    high_quality = "high_quality.png"
    history = "history.png"
    home = "home.png"
    hotel = "hotel.png"
    hot_tub = "hot_tub.png"
    hourglass_empty = "hourglass_empty.png"
    hourglass_full = "hourglass_full.png"
    http = "http.png"
    https = "https.png"
    image = "image.png"
    image_aspect_ratio = "image_aspect_ratio.png"
    important_devices = "important_devices.png"
    import_contacts = "import_contacts.png"
    import_export = "import_export.png"
    inbox = "inbox.png"
    info = "info.png"
    info_outline = "info_outline.png"
    input = "input.png"
    insert_chart = "insert_chart.png"
    insert_comment = "insert_comment.png"
    insert_drive_file = "insert_drive_file.png"
    insert_emoticon = "insert_emoticon.png"
    insert_invitation = "insert_invitation.png"
    insert_link = "insert_link.png"
    insert_photo = "insert_photo.png"
    invert_colors = "invert_colors.png"
    invert_colors_off = "invert_colors_off.png"
    iso = "iso.png"
    keyboard = "keyboard.png"
    keyboard_arrow_down = "keyboard_arrow_down.png"
    keyboard_arrow_left = "keyboard_arrow_left.png"
    keyboard_arrow_right = "keyboard_arrow_right.png"
    keyboard_arrow_up = "keyboard_arrow_up.png"
    keyboard_backspace = "keyboard_backspace.png"
    keyboard_capslock = "keyboard_capslock.png"
    keyboard_hide = "keyboard_hide.png"
    keyboard_return = "keyboard_return.png"
    keyboard_tab = "keyboard_tab.png"
    keyboard_voice = "keyboard_voice.png"
    kitchen = "kitchen.png"
    label = "label.png"
    label_outline = "label_outline.png"
    landscape = "landscape.png"
    language = "language.png"
    laptop = "laptop.png"
    laptop_chromebook = "laptop_chromebook.png"
    laptop_mac = "laptop_mac.png"
    laptop_windows = "laptop_windows.png"
    last_page = "last_page.png"
    launch = "launch.png"
    layers = "layers.png"
    layers_clear = "layers_clear.png"
    leak_add = "leak_add.png"
    leak_remove = "leak_remove.png"
    lens = "lens.png"
    library_add = "library_add.png"
    library_books = "library_books.png"
    library_musblack_48dp = "library_musblack_48dp.png"
    lightbulb_outline = "lightbulb_outline.png"
    linear_scale = "linear_scale.png"
    line_style = "line_style.png"
    line_weight = "line_weight.png"
    link = "link.png"
    linked_camera = "linked_camera.png"
    list = "list.png"
    live_help = "live_help.png"
    live_tv = "live_tv.png"
    local_activity = "local_activity.png"
    local_airport = "local_airport.png"
    local_atm = "local_atm.png"
    local_bar = "local_bar.png"
    local_cafe = "local_cafe.png"
    local_car_wash = "local_car_wash.png"
    local_convenience_store = "local_convenience_store.png"
    local_dining = "local_dining.png"
    local_drink = "local_drink.png"
    local_florist = "local_florist.png"
    local_gas_station = "local_gas_station.png"
    local_grocery_store = "local_grocery_store.png"
    local_hospital = "local_hospital.png"
    local_hotel = "local_hotel.png"
    local_laundry_service = "local_laundry_service.png"
    local_library = "local_library.png"
    local_mall = "local_mall.png"
    local_movies = "local_movies.png"
    local_offer = "local_offer.png"
    local_parking = "local_parking.png"
    local_pharmacy = "local_pharmacy.png"
    local_phone = "local_phone.png"
    local_pizza = "local_pizza.png"
    local_play = "local_play.png"
    local_post_office = "local_post_office.png"
    local_printshop = "local_printshop.png"
    local_see = "local_see.png"
    local_shipping = "local_shipping.png"
    local_taxi = "local_taxi.png"
    location_city = "location_city.png"
    location_disabled = "location_disabled.png"
    location_off = "location_off.png"
    location_on = "location_on.png"
    location_searching = "location_searching.png"
    lock = "lock.png"
    lock_open = "lock_open.png"
    lock_outline = "lock_outline.png"
    looks = "looks.png"
    looks_3 = "looks_3.png"
    looks_4 = "looks_4.png"
    looks_5 = "looks_5.png"
    looks_6 = "looks_6.png"
    looks_one = "looks_one.png"
    looks_two = "looks_two.png"
    loop = "loop.png"
    loupe = "loupe.png"
    low_priority = "low_priority.png"
    loyalty = "loyalty.png"
    mail = "mail.png"
    mail_outline = "mail_outline.png"
    map = "map.png"
    markunread = "markunread.png"
    markunread_mailbox = "markunread_mailbox.png"
    mblack_48dp = "mblack_48dp.png"
    memory = "memory.png"
    menu = "menu.png"
    merge_type = "merge_type.png"
    message = "message.png"
    mms = "mms.png"
    mnone = "mnone.png"
    mode_comment = "mode_comment.png"
    mode_edit = "mode_edit.png"
    moff = "moff.png"
    monetization_on = "monetization_on.png"
    money_off = "money_off.png"
    monochrome_photos = "monochrome_photos.png"
    mood = "mood.png"
    mood_bad = "mood_bad.png"
    more = "more.png"
    more_horiz = "more_horiz.png"
    more_vert = "more_vert.png"
    motorcycle = "motorcycle.png"
    mouse = "mouse.png"
    move_to_inbox = "move_to_inbox.png"
    movie = "movie.png"
    movie_creation = "movie_creation.png"
    movie_filter = "movie_filter.png"
    multiline_chart = "multiline_chart.png"
    musnote = "musnote.png"
    musvideo = "musvideo.png"
    my_location = "my_location.png"
    nature = "nature.png"
    nature_people = "nature_people.png"
    navigate_before = "navigate_before.png"
    navigate_next = "navigate_next.png"
    navigation = "navigation.png"
    near_me = "near_me.png"
    network_cell = "network_cell.png"
    network_check = "network_check.png"
    network_locked = "network_locked.png"
    network_wifi = "network_wifi.png"
    new_releases = "new_releases.png"
    next_week = "next_week.png"
    nfc = "nfc.png"
    note = "note.png"
    note_add = "note_add.png"
    notifications = "notifications.png"
    notifications_active = "notifications_active.png"
    notifications_none = "notifications_none.png"
    notifications_off = "notifications_off.png"
    notifications_paused = "notifications_paused.png"
    not_interested = "not_interested.png"
    no_encryption = "no_encryption.png"
    no_sim = "no_sim.png"
    offline_pin = "offline_pin.png"
    ondemand_video = "ondemand_video.png"
    opacity = "opacity.png"
    open_in_browser = "open_in_browser.png"
    open_in_new = "open_in_new.png"
    open_with = "open_with.png"
    pages = "pages.png"
    pageview = "pageview.png"
    palette = "palette.png"
    panorama = "panorama.png"
    panorama_fish_eye = "panorama_fish_eye.png"
    panorama_horizontal = "panorama_horizontal.png"
    panorama_vertical = "panorama_vertical.png"
    panorama_wide_angle = "panorama_wide_angle.png"
    pan_tool = "pan_tool.png"
    party_mode = "party_mode.png"
    pause = "pause.png"
    pause_circle_filled = "pause_circle_filled.png"
    pause_circle_outline = "pause_circle_outline.png"
    payment = "payment.png"
    people = "people.png"
    people_outline = "people_outline.png"
    perm_camera_mblack_48dp = "perm_camera_mblack_48dp.png"
    perm_contact_calendar = "perm_contact_calendar.png"
    perm_data_setting = "perm_data_setting.png"
    perm_device_information = "perm_device_information.png"
    perm_identity = "perm_identity.png"
    perm_media = "perm_media.png"
    perm_phone_msg = "perm_phone_msg.png"
    perm_scan_wifi = "perm_scan_wifi.png"
    person = "person.png"
    personal_video = "personal_video.png"
    person_add = "person_add.png"
    person_outline = "person_outline.png"
    person_pin = "person_pin.png"
    person_pin_circle = "person_pin_circle.png"
    pets = "pets.png"
    phone = "phone.png"
    phonelink = "phonelink.png"
    phonelink_erase = "phonelink_erase.png"
    phonelink_lock = "phonelink_lock.png"
    phonelink_off = "phonelink_off.png"
    phonelink_ring = "phonelink_ring.png"
    phonelink_setup = "phonelink_setup.png"
    phone_android = "phone_android.png"
    phone_bluetooth_speaker = "phone_bluetooth_speaker.png"
    phone_forwarded = "phone_forwarded.png"
    phone_in_talk = "phone_in_talk.png"
    phone_iphone = "phone_iphone.png"
    phone_locked = "phone_locked.png"
    phone_missed = "phone_missed.png"
    phone_paused = "phone_paused.png"
    photo = "photo.png"
    photo_album = "photo_album.png"
    photo_camera = "photo_camera.png"
    photo_filter = "photo_filter.png"
    photo_library = "photo_library.png"
    photo_size_select_actual = "photo_size_select_actual.png"
    photo_size_select_large = "photo_size_select_large.png"
    photo_size_select_small = "photo_size_select_small.png"
    picture_as_pdf = "picture_as_pdf.png"
    picture_in_picture = "picture_in_picture.png"
    picture_in_picture_alt = "picture_in_picture_alt.png"
    pie_chart = "pie_chart.png"
    pie_chart_outlined = "pie_chart_outlined.png"
    pin_drop = "pin_drop.png"
    place = "place.png"
    playlist_add = "playlist_add.png"
    playlist_add_check = "playlist_add_check.png"
    playlist_play = "playlist_play.png"
    play_arrow = "play_arrow.png"
    play_circle_filled = "play_circle_filled.png"
    play_circle_filled_white = "play_circle_filled_white.png"
    play_circle_outline = "play_circle_outline.png"
    play_for_work = "play_for_work.png"
    plus_one = "plus_one.png"
    poll = "poll.png"
    polymer = "polymer.png"
    pool = "pool.png"
    portable_wifi_off = "portable_wifi_off.png"
    portrait = "portrait.png"
    power = "power.png"
    power_input = "power_input.png"
    power_settings_new = "power_settings_new.png"
    pregnant_woman = "pregnant_woman.png"
    present_to_all = "present_to_all.png"
    print = "print.png"
    priority_high = "priority_high.png"
    publblack_48dp = "publblack_48dp.png"
    publish = "publish.png"
    query_builder = "query_builder.png"
    question_answer = "question_answer.png"
    queue = "queue.png"
    queue_musblack_48dp = "queue_musblack_48dp.png"
    queue_play_next = "queue_play_next.png"
    radio = "radio.png"
    rate_review = "rate_review.png"
    receipt = "receipt.png"
    recent_actors = "recent_actors.png"
    record_voice_over = "record_voice_over.png"
    redeem = "redeem.png"
    redo = "redo.png"
    refresh = "refresh.png"
    remove = "remove.png"
    remove_circle = "remove_circle.png"
    remove_circle_outline = "remove_circle_outline.png"
    remove_from_queue = "remove_from_queue.png"
    remove_red_eye = "remove_red_eye.png"
    remove_shopping_cart = "remove_shopping_cart.png"
    reorder = "reorder.png"
    repeat = "repeat.png"
    repeat_one = "repeat_one.png"
    replay = "replay.png"
    replay_10 = "replay_10.png"
    replay_30 = "replay_30.png"
    replay_5 = "replay_5.png"
    reply = "reply.png"
    reply_all = "reply_all.png"
    report = "report.png"
    report_problem = "report_problem.png"
    restaurant = "restaurant.png"
    restaurant_menu = "restaurant_menu.png"
    restore = "restore.png"
    restore_page = "restore_page.png"
    ring_volume = "ring_volume.png"
    room = "room.png"
    room_service = "room_service.png"
    rotate_90_degrees_ccw = "rotate_90_degrees_ccw.png"
    rotate_left = "rotate_left.png"
    rotate_right = "rotate_right.png"
    rounded_corner = "rounded_corner.png"
    router = "router.png"
    rowing = "rowing.png"
    rss_feed = "rss_feed.png"
    rv_hookup = "rv_hookup.png"
    satellite = "satellite.png"
    save = "save.png"
    scanner = "scanner.png"
    schedule = "schedule.png"
    school = "school.png"
    screen_lock_landscape = "screen_lock_landscape.png"
    screen_lock_portrait = "screen_lock_portrait.png"
    screen_lock_rotation = "screen_lock_rotation.png"
    screen_rotation = "screen_rotation.png"
    screen_share = "screen_share.png"
    sd_card = "sd_card.png"
    sd_storage = "sd_storage.png"
    search = "search.png"
    security = "security.png"
    select_all = "select_all.png"
    send = "send.png"
    sentiment_dissatisfied = "sentiment_dissatisfied.png"
    sentiment_neutral = "sentiment_neutral.png"
    sentiment_satisfied = "sentiment_satisfied.png"
    sentiment_very_dissatisfied = "sentiment_very_dissatisfied.png"
    sentiment_very_satisfied = "sentiment_very_satisfied.png"
    settings = "settings.png"
    settings_applications = "settings_applications.png"
    settings_backup_restore = "settings_backup_restore.png"
    settings_bluetooth = "settings_bluetooth.png"
    settings_brightness = "settings_brightness.png"
    settings_cell = "settings_cell.png"
    settings_ethernet = "settings_ethernet.png"
    settings_input_antenna = "settings_input_antenna.png"
    settings_input_component = "settings_input_component.png"
    settings_input_composite = "settings_input_composite.png"
    settings_input_hdmi = "settings_input_hdmi.png"
    settings_input_svideo = "settings_input_svideo.png"
    settings_overscan = "settings_overscan.png"
    settings_phone = "settings_phone.png"
    settings_power = "settings_power.png"
    settings_remote = "settings_remote.png"
    settings_system_daydream = "settings_system_daydream.png"
    settings_voice = "settings_voice.png"
    share = "share.png"
    shop = "shop.png"
    shopping_basket = "shopping_basket.png"
    shopping_cart = "shopping_cart.png"
    shop_two = "shop_two.png"
    short_text = "short_text.png"
    show_chart = "show_chart.png"
    shuffle = "shuffle.png"
    signal_cellular_0_bar = "signal_cellular_0_bar.png"
    signal_cellular_1_bar = "signal_cellular_1_bar.png"
    signal_cellular_2_bar = "signal_cellular_2_bar.png"
    signal_cellular_3_bar = "signal_cellular_3_bar.png"
    signal_cellular_4_bar = "signal_cellular_4_bar.png"
    signal_cellular_connected_no_internet_0_bar = "signal_cellular_connected_no_internet_0_bar.png"
    signal_cellular_connected_no_internet_1_bar = "signal_cellular_connected_no_internet_1_bar.png"
    signal_cellular_connected_no_internet_2_bar = "signal_cellular_connected_no_internet_2_bar.png"
    signal_cellular_connected_no_internet_3_bar = "signal_cellular_connected_no_internet_3_bar.png"
    signal_cellular_connected_no_internet_4_bar = "signal_cellular_connected_no_internet_4_bar.png"
    signal_cellular_no_sim = "signal_cellular_no_sim.png"
    signal_cellular_null = "signal_cellular_null.png"
    signal_cellular_off = "signal_cellular_off.png"
    signal_wifi_0_bar = "signal_wifi_0_bar.png"
    signal_wifi_1_bar = "signal_wifi_1_bar.png"
    signal_wifi_1_bar_lock = "signal_wifi_1_bar_lock.png"
    signal_wifi_2_bar = "signal_wifi_2_bar.png"
    signal_wifi_2_bar_lock = "signal_wifi_2_bar_lock.png"
    signal_wifi_3_bar = "signal_wifi_3_bar.png"
    signal_wifi_3_bar_lock = "signal_wifi_3_bar_lock.png"
    signal_wifi_4_bar = "signal_wifi_4_bar.png"
    signal_wifi_4_bar_lock = "signal_wifi_4_bar_lock.png"
    signal_wifi_off = "signal_wifi_off.png"
    sim_card = "sim_card.png"
    sim_card_alert = "sim_card_alert.png"
    skip_next = "skip_next.png"
    skip_previous = "skip_previous.png"
    slideshow = "slideshow.png"
    slow_motion_video = "slow_motion_video.png"
    smartphone = "smartphone.png"
    smoke_free = "smoke_free.png"
    smoking_rooms = "smoking_rooms.png"
    sms = "sms.png"
    sms_failed = "sms_failed.png"
    snooze = "snooze.png"
    sort = "sort.png"
    sort_by_alpha = "sort_by_alpha.png"
    spa = "spa.png"
    space_bar = "space_bar.png"
    speaker = "speaker.png"
    speaker_group = "speaker_group.png"
    speaker_notes = "speaker_notes.png"
    speaker_notes_off = "speaker_notes_off.png"
    speaker_phone = "speaker_phone.png"
    spellcheck = "spellcheck.png"
    star = "star.png"
    stars = "stars.png"
    star_border = "star_border.png"
    star_half = "star_half.png"
    stay_current_landscape = "stay_current_landscape.png"
    stay_current_portrait = "stay_current_portrait.png"
    stay_primary_landscape = "stay_primary_landscape.png"
    stay_primary_portrait = "stay_primary_portrait.png"
    stop = "stop.png"
    stop_screen_share = "stop_screen_share.png"
    storage = "storage.png"
    store = "store.png"
    store_mall_directory = "store_mall_directory.png"
    straighten = "straighten.png"
    streetview = "streetview.png"
    strikethrough_s = "strikethrough_s.png"
    style = "style.png"
    subdirectory_arrow_left = "subdirectory_arrow_left.png"
    subdirectory_arrow_right = "subdirectory_arrow_right.png"
    subject = "subject.png"
    subscriptions = "subscriptions.png"
    subtitles = "subtitles.png"
    subway = "subway.png"
    supervisor_account = "supervisor_account.png"
    surround_sound = "surround_sound.png"
    swap_calls = "swap_calls.png"
    swap_horiz = "swap_horiz.png"
    swap_vert = "swap_vert.png"
    swap_vertical_circle = "swap_vertical_circle.png"
    switch_camera = "switch_camera.png"
    switch_video = "switch_video.png"
    sync = "sync.png"
    sync_disabled = "sync_disabled.png"
    sync_problem = "sync_problem.png"
    system_update = "system_update.png"
    system_update_alt = "system_update_alt.png"
    tab = "tab.png"
    tablet = "tablet.png"
    tablet_android = "tablet_android.png"
    tablet_mac = "tablet_mac.png"
    tab_unselected = "tab_unselected.png"
    tag_faces = "tag_faces.png"
    tap_and_play = "tap_and_play.png"
    terrain = "terrain.png"
    textsms = "textsms.png"
    texture = "texture.png"
    text_fields = "text_fields.png"
    text_format = "text_format.png"
    theaters = "theaters.png"
    thumbs_up_down = "thumbs_up_down.png"
    thumb_down = "thumb_down.png"
    thumb_up = "thumb_up.png"
    timelapse = "timelapse.png"
    timeline = "timeline.png"
    timer = "timer.png"
    timer_10 = "timer_10.png"
    timer_3 = "timer_3.png"
    timer_off = "timer_off.png"
    time_to_leave = "time_to_leave.png"
    title = "title.png"
    toc = "toc.png"
    today = "today.png"
    toll = "toll.png"
    tonality = "tonality.png"
    touch_app = "touch_app.png"
    toys = "toys.png"
    track_changes = "track_changes.png"
    traffblack_48dp = "traffblack_48dp.png"
    train = "train.png"
    tram = "tram.png"
    transfer_within_a_station = "transfer_within_a_station.png"
    transform = "transform.png"
    translate = "translate.png"
    trending_down = "trending_down.png"
    trending_flat = "trending_flat.png"
    trending_up = "trending_up.png"
    tune = "tune.png"
    turned_in = "turned_in.png"
    turned_in_not = "turned_in_not.png"
    tv = "tv.png"
    unarchive = "unarchive.png"
    undo = "undo.png"
    unfold_less = "unfold_less.png"
    unfold_more = "unfold_more.png"
    update = "update.png"
    usb = "usb.png"
    verified_user = "verified_user.png"
    vertical_align_bottom = "vertical_align_bottom.png"
    vertical_align_center = "vertical_align_center.png"
    vertical_align_top = "vertical_align_top.png"
    vibration = "vibration.png"
    videocam = "videocam.png"
    videocam_off = "videocam_off.png"
    videogame_asset = "videogame_asset.png"
    video_call = "video_call.png"
    video_label = "video_label.png"
    video_library = "video_library.png"
    view_agenda = "view_agenda.png"
    view_array = "view_array.png"
    view_carousel = "view_carousel.png"
    view_column = "view_column.png"
    view_comfy = "view_comfy.png"
    view_compact = "view_compact.png"
    view_day = "view_day.png"
    view_headline = "view_headline.png"
    view_list = "view_list.png"
    view_module = "view_module.png"
    view_quilt = "view_quilt.png"
    view_stream = "view_stream.png"
    view_week = "view_week.png"
    vignette = "vignette.png"
    visibility = "visibility.png"
    visibility_off = "visibility_off.png"
    voicemail = "voicemail.png"
    voice_chat = "voice_chat.png"
    volume_down = "volume_down.png"
    volume_mute = "volume_mute.png"
    volume_off = "volume_off.png"
    volume_up = "volume_up.png"
    vpn_key = "vpn_key.png"
    vpn_lock = "vpn_lock.png"
    wallpaper = "wallpaper.png"
    warning = "warning.png"
    watch = "watch.png"
    watch_later = "watch_later.png"
    wb_auto = "wb_auto.png"
    wb_cloudy = "wb_cloudy.png"
    wb_incandescent = "wb_incandescent.png"
    wb_iridescent = "wb_iridescent.png"
    wb_sunny = "wb_sunny.png"
    wc = "wc.png"
    web = "web.png"
    web_asset = "web_asset.png"
    weekend = "weekend.png"
    whatshot = "whatshot.png"
    widgets = "widgets.png"
    wifi = "wifi.png"
    wifi_lock = "wifi_lock.png"
    wifi_tethering = "wifi_tethering.png"
    work = "work.png"
    wrap_text = "wrap_text.png"
    youtube_searched_for = "youtube_searched_for.png"
    zoom_in = "zoom_in.png"
    zoom_out = "zoom_out.png"
    zoom_out_map = "zoom_out_map.png"

c = Color
i = Icons

def get(color, name):
    base_folder = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_folder, color, name)