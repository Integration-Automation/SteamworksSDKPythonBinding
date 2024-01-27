import ctypes

from steamworks.exceptions import *


class SteamUGCQuery(object):
    class SteamUGCDetails_t(ctypes.Structure):
        _fields_ = [
            ("m_nPublishedFileId", ctypes.c_uint64),
            ("m_eResult", ctypes.c_uint),
            ("m_eFileType", ctypes.c_uint),
            ("m_nCreatorAppID", ctypes.c_uint),
            ("m_nConsumerAppID", ctypes.c_uint),
            ("m_rgchTitle", ctypes.c_char_p),
            ("m_rgchDescription", ctypes.c_char_p),
            ("m_ulSteamIDOwner", ctypes.c_uint64),
            ("m_rtimeCreated", ctypes.c_uint32),
            ("m_rtimeUpdated", ctypes.c_uint32),
            ("m_rtimeAddedToUserList", ctypes.c_uint32),
            ("m_eVisibility", ctypes.c_uint),
            ("m_bBanned", ctypes.c_bool),
            ("m_bAcceptedForUse", ctypes.c_bool),
            ("m_bTagsTruncated", ctypes.c_bool),
            ("m_rgchTags", ctypes.c_char_p),
            ("m_hFile", ctypes.c_uint64),
            ("m_hPreviewFile", ctypes.c_uint64),
            ("m_pchFileName", ctypes.c_char_p),
            ("m_nFileSize", ctypes.c_int32),
            ("m_nPreviewFileSize", ctypes.c_int32),
            ("m_rgchURL", ctypes.c_char_p),
            ("m_unVotesUp", ctypes.c_uint32),
            ("m_unVotesDown", ctypes.c_uint32),
            ("m_flScore", ctypes.c_float),
            ("m_unNumChildren", ctypes.c_uint32)
        ]

    def __init__(self, steam: object):
        self.steam = steam
        if not self.steam.loaded():
            raise SteamNotLoadedException('STEAMWORKS not yet loaded')

    def create_query_user_ugc_request(self, un_account_id: int, e_list_type: int, e_matching_ugc_typ: int,
                                      e_sort_order: int, n_creator_app_id: int, n_consumer_app_id: int, un_page: int):
        return self.steam.CreateQueryUserUGCRequest(un_account_id, e_list_type, e_matching_ugc_typ, e_sort_order,
                                                    n_creator_app_id, n_consumer_app_id, un_page)

    def create_query_all_ugc_request(self, e_query_type: int, e_matchinge_matching_ugc_type_file_type: int,
                                     n_creator_app_id: int, n_consumer_app_id: int, un_page: int):
        return self.steam.CreateQueryAllUGCRequest(e_query_type, e_matchinge_matching_ugc_type_file_type,
                                                   n_creator_app_id, n_consumer_app_id, un_page)

    def create_query_ugc_details_request(self, pvec_published_file_id: int, un_num_published_file_i_ds: int):
        return self.steam.CreateQueryUGCDetailsRequest(pvec_published_file_id, un_num_published_file_i_ds)

    def set_cloud_file_name_filter(self, handle: int, p_match_cloud_file_name: str):
        return self.steam.SetCloudFileNameFilter(handle, p_match_cloud_file_name)

    def set_match_any_tag(self, handle: int, b_match_any_tag: bool):
        return self.steam.SetMatchAnyTag(handle, b_match_any_tag)

    def set_search_text(self, handle: int, p_search_text: str):
        return self.steam.SetSearchText(handle, p_search_text)

    def set_ranked_by_trend_days(self, handle: int, un_days: int):
        return self.steam.SetRankedByTrendDays(handle, un_days)

    def add_required_tag(self, handle: int, p_tag_name: str):
        return self.steam.AddRequiredTag(handle, p_tag_name)

    def add_excluded_tag(self, handle: int, p_tag_name: str):
        return self.steam.AddExcludedTag(handle, p_tag_name)

    def add_required_key_value_tag(self, handle: int, p_key: str, p_value: str):
        return self.steam.AddRequiredKeyValueTag(handle, p_key, p_value)

    def set_return_only_ids(self, handle: int, b_return_only_ids: bool):
        return self.steam.SetReturnOnlyIDs(handle, b_return_only_ids)

    def set_return_key_value_tags(self, handle: int, b_return_key_value_tags: bool):
        return self.steam.SetReturnKeyValueTags(handle, b_return_key_value_tags)

    def set_return_long_description(self, handle: int, b_return_long_description: bool):
        return self.steam.SetReturnLongDescription(handle, b_return_long_description)

    def set_return_metadata(self, handle: int, b_return_metadata: bool):
        return self.steam.SetReturnMetadata(handle, b_return_metadata)

    def set_return_children(self, handle: int, b_return_children: bool):
        return self.steam.SetReturnChildren(handle, b_return_children)

    def set_return_additional_previews(self, handle: int, b_return_additional_previews: bool):
        return self.steam.SetReturnAdditionalPreviews(handle, b_return_additional_previews)

    def set_return_total_only(self, handle: int, b_return_total_only: bool):
        return self.steam.SetReturnTotalOnly(handle, b_return_total_only)

    def set_language(self, handle: int, pch_language: str):
        return self.steam.SetLanguage(handle, pch_language)

    def set_allow_cached_response(self, handle: int, un_max_age_seconds: int):
        return self.steam.SetAllowCachedResponse(handle, un_max_age_seconds)

    def send_query_ugc_request(self, handle: int):
        return self.steam.SendQueryUGCRequest(handle)

    def get_query_ugc_result(self, handle: int, index: int, p_details: SteamUGCDetails_t):
        return self.steam.GetQueryUGCResult(handle, index, p_details)

    def release_query_ugc_request(self, handle: int):
        return self.steam.ReleaseQueryUGCRequest(handle)

    def get_query_ugc_preview_url(self, handle: int, index: int, pch_url: str, cch_url_size: int):
        return self.steam.GetQueryUGCPreviewURL(handle, index, pch_url, cch_url_size)

    def get_query_ugc_metadata(self, handle: int, index: int, pch_url: str, cch_metadatasize: int):
        return self.steam.GetQueryUGCMetadata(handle, index, pch_url, cch_metadatasize)

    def get_query_ugc_children(self, handle: int, index: int, pvec_published_file_id: int, c_max_entries: int):
        return self.steam.GetQueryUGCChildren(handle, index, pvec_published_file_id, c_max_entries)

    def get_query_ugc_statistic(self, handle: int, index: int, e_stat_type: int, p_stat_value: int):
        return self.steam.GetQueryUGCStatistic(handle, index, e_stat_type, p_stat_value)

    def get_query_ugc_additional_preview(
            self, handle: int, index: int, preview_index: int, pch_url_or_video_id: str, cch_url_size: int,
            pch_original_file_name: str, cch_original_file_name_size: int, p_preview_type: int):
        return self.steam.GetQueryUGCAdditionalPreview(
            handle, index, preview_index, pch_url_or_video_id, cch_url_size, pch_original_file_name,
            cch_original_file_name_size, p_preview_type)

    def get_query_ugc_key_value_tag(self, handle: int, index: int, key_value_tag_index: int, pch_key: str,
                                    cch_key_size: int, cch_value_size: int):
        return self.steam.GetQueryUGCKeyValueTag(
            handle, index, key_value_tag_index, pch_key, cch_key_size, cch_value_size)

    def get_query_ugc_num_additional_previews(self, handle: int, index: int):
        return self.steam.GetQueryUGCNumAdditionalPreviews(handle, index)

    def get_query_ugc_num_key_value_tags(self, handle: int, index: int):
        return self.steam.GetQueryUGCNumKeyValueTags(handle, index)
