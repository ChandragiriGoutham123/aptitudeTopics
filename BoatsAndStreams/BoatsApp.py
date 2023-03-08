print("Select one among below  : ")
enter_value_you_want_to_find = input("1.Stream or current Speed \n""2.Boat or Man Speed\n"
                                     "3.Distance\n""4.Time\n""5.Ratios\n""6.Average speeds:")
if enter_value_you_want_to_find == "1":
    inputs = input("1.inputs = Along stream speed,along stream time, against stream speed, against stream time\n"
                   "2.inputs = speed of boat ,upstream distance,downstream distance\n""3.inputs = total distance,"
                   "total time,some distance with stream ,some distance down stream\n""4.inputs = two upstream distances"
                   ",two downstream distances,two times\n""5.inputs = cross river perpendicularly\n"
                   "6.inputs = same distance,upstream time,Down stream time : ")
    if inputs == "1" or inputs == "2" or inputs == "6":
        import along_and_against

        print(along_and_against.alongAndAgainst)
    elif inputs == "3":
        import when_total_distance_part_of_distance_time_given

        print(when_total_distance_part_of_distance_time_given.totalDistancePartOfDistanceTime)
    elif inputs == "4":
        import when_upstream_distance_and_downstream_distance_given

        print(when_upstream_distance_and_downstream_distance_given.upstreamDistanceDownstreamDistance)
    elif inputs == "5":
        import when_river_cross_perpenduclurly

        print(when_river_cross_perpenduclurly.riverCrossPerpendicularly)
elif enter_value_you_want_to_find == "2":
    inputs = input("1.inputs = Along stream speed,along stream time, against stream speed, against stream time\n"
                   "2.inputs = same distance,upstream time,Down stream time\n""3.inputs = only stream flow is given\n"
                   "4.inputs = upstream distance,upstream time ,speed of stream\n""5.inputs = mans speed with current "
                   ",speed of current\n""5.inputs = mans rate,against current rate\n""6.inputs = upstream time,"
                   "downstream time,speed of stream\n""7.inputs = two upstream distances"
                   ",two downstream distances,two times\n""8.inputs = downstream speed,upstream speed: ")
    if inputs == "1" or inputs == "2" or inputs == "8":
        import along_and_against

        print(along_and_against.alongAndAgainst)
    elif inputs == "3":
        import when_only_stream_flow_is_given

        print(when_only_stream_flow_is_given.onlyStreamFlowIsGiven)
    elif inputs == "4":
        import against

        print(against.against)
    elif inputs == "5":
        import when_man_speed_with_current_and_current_speed_given

        print(when_man_speed_with_current_and_current_speed_given.manSpeedWithCurrentAndCurrentSpeed)
    elif inputs == "6":
        import when_mans_rate_and_against_current_rate_given

        print(when_mans_rate_and_against_current_rate_given.mansRateAndAgainstCurrentRate)
    elif inputs == "7":
        import when_upstream_distance_and_downstream_distance_given

        print(when_upstream_distance_and_downstream_distance_given.upstreamDistanceDownstreamDistance)

elif enter_value_you_want_to_find == "3":
    inputs = input("1.inputs = downstream boat speed,downstream stream speed,downstream time\n""2.inputs = mans speed,"
                   "current speed,total time\n""3.inputs = three points given(a,b,c),time,stream speed,boat speed: ")
    if inputs == "1":
        import along

        print(along.along)
    elif inputs == "2" or inputs == "3":
        import when_same_distance_speed_of_boat_speed_of_stream_given

        print(when_same_distance_speed_of_boat_speed_of_stream_given.sameDistanceSpeedOfBoatSpeedOfStream)


elif enter_value_you_want_to_find == "4":
    inputs = input(
        "1.inputs = down stream distance,downstream speed,upstream speed,upstream distance ,to find for different"
        "distance\n""2.inputs = upstream distance,upstream speed,upstream time\n""3.inputs = same distance,speed of boat"
        ",speed of stream\n""4.inputs = width of river,man speed,current speed\n""5.inputs = upstream distance"
        ",upstream stream speed,upstream time,for different distance: ")
    if inputs == "1" or inputs == "5":
        import along_and_against

        print(along_and_against.alongAndAgainst)
    elif inputs == "2":
        import against

        print(against.against)
    elif inputs == "3":
        import when_same_distance_speed_of_boat_speed_of_stream_given

        print(when_same_distance_speed_of_boat_speed_of_stream_given.sameDistanceSpeedOfBoatSpeedOfStream)
    elif inputs == "4":
        import when_width_of_river_and_rate_of_man_given

        print(when_width_of_river_and_rate_of_man_given.widthOfRiverRateOfMan)


elif enter_value_you_want_to_find == "5":
    inputs = input(
        "1.inputs = boat takes half time moving certain distance downstream and upstream\n""2.inputs = upstream time,"
        "downstream time\n""2.inputs = three points(p,q,r),upstream time,downstream time: ")
    if inputs == "1":
        import half_time_taken_to_down_stream_than_upstream

        print(half_time_taken_to_down_stream_than_upstream.halfTimeTakenToDownstreamThanUpstream)
    elif inputs == "2" or inputs == "3":
        import when_upstream_time_and_downstream_time_given

        print(when_upstream_time_and_downstream_time_given.upstreamTimeDownstreamTime)

elif enter_value_you_want_to_find == "7":
    import when_distance_average_speed_and_time_given

    print(when_distance_average_speed_and_time_given.distanceAverageSpeedAndTime)
